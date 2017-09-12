from twilio.rest import Client
from .. import app
import random

def send_confirmation_code(to_number):
    verification_code = generate_code()
    send_sms(to_number, verification_code)
    return verification_code