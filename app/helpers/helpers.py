from twilio.rest import Client
from .. import app
import random
from app.models.models import User
import datetime


def send_confirmation_code(to_number, code):
    verification_code = code
    to_number = "{}{}".format("+91", to_number)
    send_sms(to_number, verification_code)

def generate_code():
    return str(random.randrange(1000, 9999))


def send_sms(to_number, body):
    account_sid = app.config['TWILIO_ACCOUNT_SID']
    auth_token = app.config['TWILIO_AUTH_TOKEN']
    twilio_number = app.config['TWILIO_NUMBER']
    client = Client(account_sid, auth_token)
    client.api.messages.create(to_number,
                           from_=twilio_number,
                           body=body)


def create_mobile_user(mobile_no):
    new_user = User(mobile_no=mobile_no,
                    otp=generate_code(),
                    is_verified=False,
                    created_at=datetime.datetime.now()
                    )
    return new_user