from twilio.rest import Client
from .. import app
import random
from app.models.models import User
import datetime


class Helper(object):
    """Helper Class"""

    def send_confirmation_code(self, to_number, code):
        """
        Sends confirmation code(or OTP) to user's mobile address
        Args:
             to_number: The mobile number to send the OTP to
             code: OTP
        """
        verification_code = code
        to_number = "{}{}".format("+91", to_number)
        self.send_sms(to_number, verification_code)

    def generate_code(self):
        """
        Generates 4 digit code to send as OTP to user's mobile
        Returns:
            A string of 4 digits
        """
        return str(random.randrange(1000, 9999))

    def send_sms(self, to_number, body):
        """
        Send sms to user's mobile number
        Args:
            to_number: The mobile number to send the SMS to
            body: The message
        """
        account_sid = app.config['TWILIO_ACCOUNT_SID']
        auth_token = app.config['TWILIO_AUTH_TOKEN']
        twilio_number = app.config['TWILIO_NUMBER']
        client = Client(account_sid, auth_token)
        client.api.messages.create(to_number,
                                   from_=twilio_number,
                                   body=body)

    def create_mobile_user(self, mobile_no):
        """
        Creates a new user to commit to the database
        Args:
            mobile_no: Mobile number to save to database
        Returns:
            A User instance
        """
        new_user = User(mobile_no=mobile_no,
                        otp=self.generate_code(),
                        is_verified=False,
                        created_at=datetime.datetime.now()
                        )
        return new_user


# Helper object
helper = Helper()
