from flask import Flask
import string
import random
# from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER

app = Flask(__name__)

from .mod_auth.auth import mod_auth

secret_key = ''.join(random.choice(
    string.ascii_uppercase + string.digits) for x in range(32))

app.register_blueprint(mod_auth)

app.config.from_object('config.Config')

# app.config['SECRET_KEY'] = secret_key