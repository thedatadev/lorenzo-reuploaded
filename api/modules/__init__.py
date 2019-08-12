from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

from modules.account_module.routes import mod as account_mod
from modules.chatbot_module.routes import mod as chatbot_mod
from modules.search_module.routes import mod as search_mod
from modules.booking_module.routes import mod as booking_mod
from modules.advertise_module.routes import mod as advertise_mod
from modules.database_module.shared_db import db

app = Flask(__name__)
## Enable CORS
CORS(app)
## Register blueprints (modules)
app.register_blueprint(account_mod)
app.register_blueprint(chatbot_mod)
app.register_blueprint(search_mod)
app.register_blueprint(booking_mod)
app.register_blueprint(advertise_mod)
# Set app config
app.config.from_object('settings.config')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "settings/diagtest-2a717a8d941e.json"

# Initialize database
db.init_app(app)
