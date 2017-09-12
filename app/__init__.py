from flask import Flask

app = Flask(__name__)

from .mod_auth.auth import mod_auth

app.register_blueprint(mod_auth)

app.config.from_object('config.Config')
