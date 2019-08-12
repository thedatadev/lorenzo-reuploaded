import dialogflow_v2 as dialogflow

class Chatbot():
    ''' Chatbot parses user messages and extracts entities NOTE: (tentative definition) '''

    def __init__(self):
        self.project_id = "diagtest-214406"
        self.language_code = "en-US"

    def parse(self, message, conversation_id):
        ''' Given a user message/query, parse the parameters and generate a chatbot response '''
        texts = [message] # texts parameter must be a list of string(s)
        response, params = self.detect_intent_and_generate_response(texts, conversation_id)
        return response, params

    def detect_intent_and_generate_response(self, texts, session_id):
        """ Returns the result of detect intent with texts as inputs.

        Using the same `session_id` between requests allows continuation
        of the conversation. """

        ## Track conversations using user session ID
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(self.project_id, session_id)

        ## User input messages
        for text in texts:
            # Serialize text as dialogflow.types.TextInput
            text_input = dialogflow.types.TextInput(text=text, language_code=self.language_code)
            # Recognize the text input as a query
            query_input = dialogflow.types.QueryInput(text=text_input)
            # Send the query off to DialogFlow and wait for a response
            intents_payload = session_client.detect_intent(session=session, query_input=query_input)
            # Extract the chatbot text response and parameters
            chatbot_response = intents_payload.query_result.fulfillment_text
            chatbot_params = intents_payload.query_result.parameters
            
        # return the chatbot response and parameters
        return chatbot_response, chatbot_params