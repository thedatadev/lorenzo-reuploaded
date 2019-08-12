from flask import jsonify, request
from flask import current_app as app  # Note: only available inside context of a request
import datetime
import jwt

from modules.account_module import mod
from modules.database_module.shared_db import db
from modules.database_module.models import User


## Register a new account
@mod.route("/register", methods=['POST'])
def register():
    # Receive credentials from client
    registration = request.json
    # Check all necessary fields are provided
    if not ('username' in registration and 'email' in registration
            and 'password' in registration):
        return '', 401
    # Extract user credentials
    username = registration['username']
    email = registration['email']
    password = registration['password']
    if db.session.query(User).filter_by(email=email).first():
        return '', 401
    # Save new user to main.db
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message='Registration successful'), 200


## Log into an account
@mod.route("/login", methods=['POST'])
def login():
    # Receive credentials from client
    login = request.json
    # Extract email and password from HTTP POST request
    email = login['email']
    password = login['password']
    # Retrieve user ID to store in JWT
    user = db.session.query(User).filter_by(email=email).first()
    # Verify user
    if not user:
        return '', 401
    if user.password != str(password):
        return '', 401
    # If so, create and return a new JSON Web Token (JWT)
    token = jwt.encode({ 'user': user.id, 'exp': datetime.datetime.utcnow() + \
            datetime.timedelta(minutes=180)}, app.secret_key, algorithm='HS256' )
    return jsonify(token=token.decode(), username=user.username), 200
