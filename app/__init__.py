from flask import Flask
import string
import random

app = Flask(__name__)

from .mod_auth.auth import mod_auth

secret_key = ''.join(random.choice(
    string.ascii_uppercase + string.digits) for x in range(32))

app.register_blueprint(mod_auth)

app.config['SECRET_KEY'] = secret_key