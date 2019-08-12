from flask import jsonify, request
from flask import current_app as app
import jwt
import json
from google.protobuf.json_format import MessageToJson

from modules.shared_methods import login_required, serialize, deserialize
from modules.chatbot_module import mod
from modules.database_module.shared_db import db
from modules.database_module.models import User, Conversation

from modules.chatbot_module.agent import Chatbot

chatbot = Chatbot()

def extract_required_params(params, ch=None):
    cleaned_params = {}
    if ch:
        cleaned_params = ch
    fields = ['suburbs', 'accomodation', 'date', 'accommondates', 'price_ent', 'duration']
    for field in fields:
        if field in params:
            if params[field]:
                cleaned_params[field] = params[field]
    return cleaned_params

@mod.route("/conversation", methods=['POST'])
@login_required
def new_conversation():
    ''' Initiate a new conversation between the user and the chatbot agent '''
    # Identify user
    token = request.headers.get('AUTH_TOKEN')
    decode_token = jwt.decode(token, app.secret_key)
    user_id = decode_token['user']
    # Retrieve the user
    user = db.session.query(User).filter_by(id=user_id).first()
    # Instantiate a new conversation
    new_conversation = Conversation(
        user=user, chat_history=serialize([]), query_params='')
    db.session.add(new_conversation)
    db.session.commit()
    # Return the conversation ID to the user
    print("New conversation ID:", new_conversation.id)
    return jsonify(conversation_id=new_conversation.id), 200


@mod.route("/message", methods=['POST'])
@login_required
def new_message():
    ''' Receive a new message from the user for a given conversation '''
    # Extract new message
    request_data = request.json
    message_content = request_data['content']
    # Identify conversation
    conversation_id = request_data['conversation_id']
    # Retrieve conversation
    conversation = db.session.query(Conversation).filter_by(
        id=conversation_id).first()
    # Extract entities and generate response
    chatbot_response, params = chatbot.parse(message_content, conversation_id)
    # Update query params with newly extracted entities
    conversation.query_params = serialize(params)
    # Update conversation with new messages and params
    db.session.commit()
    # Extract main params to display on frontend
    updated_params = extract_required_params(json.loads(
                     MessageToJson(deserialize(conversation.query_params))))
    # Return 200 OK
    return jsonify(chatbot_response=chatbot_response, params=updated_params), 200

@mod.route("/chatparams/<int:conversation_id>", methods=['GET'])
@login_required
def get_chat_params(conversation_id):
    ''' Retrieving the set of search paramaters belonging to a given conversation '''
    # Retrieve conversation
    conversation = db.session.query(Conversation).filter_by(
        id=conversation_id).first()
    # Deserialize the chat history
    chat_history = deserialize(conversation.chat_history)
    chatbot_response = chat_history[-1]['content'] if len(chat_history) else "Hi there!"
    params = {}
    if len(conversation.query_params):
        params = extract_required_params(json.loads(MessageToJson(deserialize(conversation.query_params))))
    # Return the chat history
    return jsonify(chatbot_response=chatbot_response, params=params), 200

@mod.route("/chatparams/<int:conversation_id>", methods=['PUT'])
@login_required
def update_chat_params(conversation_id):
    ''' Updating the set of search paramaters belonging to a given conversation '''
    # Retrieve conversation
    conversation = db.session.query(Conversation).filter_by(
        id=conversation_id).first()
    # Retrieve query_params
    update_params = deserialize(conversation.query_params)
    # Update fields
    update_fields = request.json
    for field in update_fields:
        update_params[field] = update_fields[field]
    # Commit changes
    conversation.query_params = serialize(update_params)
    db.session.commit()
    # Ensure params are JSON serializable
    params = json.loads(MessageToJson(update_params))
    return jsonify(params=params)

@mod.route("/chathistory", methods=['GET'])
@login_required
def get_all_chat_history():
    ''' Retrieve all the user's conversations '''
    token = request.headers.get("AUTH_TOKEN")
    data = jwt.decode(token, app.secret_key)
    user_id = data['user']
    user_conversations = db.session.query(Conversation).filter_by(user_id=user_id).all()
    chat_histories = []
    for conversation in user_conversations:
        # Retrieve the conversation's parameters
        chat_history = {'id': conversation.id}
        if len(conversation.query_params):
            params = deserialize(conversation.query_params)
            params = json.loads(MessageToJson(params))
            chat_history = extract_required_params(params, chat_history)        
        chat_histories.append(chat_history)
    # Conversations with larger IDs are more recent
    chat_histories = sorted(chat_histories, reverse=True, key=lambda x: x['id'])
    return jsonify(chat_histories=chat_histories), 200