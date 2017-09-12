import json
import re
import datetime
from flask import (Blueprint, render_template, request, make_response)
from app.models.models import User
from app.models.session import session
from app.helpers.helpers import helper

mod_auth = Blueprint('auth', __name__)


@mod_auth.route('/sms_verification', methods=['GET', 'POST'])
def sms_verification():
    """
    Sends the confirmation code to mobile number for verification
    """
    if request.method == 'POST':
        mobile_no = request.form.get('mobile')
        # Check for valid mobile number
        if not re.match(r'[789]\d{9}$', mobile_no):
            response = make_response(json.dumps('Invalid mobile number!'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response
        else:
            user = session.query(User).filter_by(mobile_no=mobile_no).first()
            # If user is verified
            if user is not None and user.is_verified:
                response = make_response(json.dumps(
                    "Mobile number is already verified."), 200)
                response.headers['Content-Type'] = 'application/json'
                return response
            # If user doesn't exist
            if user is None:
                new_user = helper.create_mobile_user(mobile_no)
                session.add(new_user)
                session.commit()
                print(new_user.mobile_no)
                helper.send_confirmation_code(new_user.mobile_no, new_user.otp)
            # If user is not verified
            elif user is not None and not user.is_verified:
                print(user.mobile_no)
                user.otp = helper.generate_code()
                session.add(user)
                session.commit()
                helper.send_confirmation_code(user.mobile_no, user.otp)
            response = make_response(json.dumps(
                "OTP sent to your Mobile Number"), 200)
            response.headers['Content-Type'] = 'application/json'
            return response
    else:
        return render_template("main.html")


@mod_auth.route('/mobile_otp_verification', methods=['GET', 'POST'])
def verify_user():
    """
    Verify user and update user data in the database
    """
    if request.method == 'POST':
        mobile_no = int(request.form.get('mobile'))
        otp = int(request.form.get('otp'))
        user = session.query(User).filter_by(mobile_no=mobile_no).first()
        # If user is not verified
        if user is not None and not user.is_verified:
            # Check if otp is same as that in database
            if user.otp == otp:
                user.is_verified = True
                user.updated_at = datetime.datetime.now()
                session.add(user)
                session.commit()
                response = make_response(json.dumps(
                    "Mobile number Verified."), 200)
                response.headers['Content-Type'] = 'application/json'
                return response
            else:
                response = make_response(json.dumps(
                    "Mobile number not Verified, Retry"), 200)
                response.headers['Content-Type'] = 'application/json'
                return response
        # If user is verified
        elif user is not None and user.is_verified:
            response = make_response(json.dumps(
                "Mobile number already Verified."), 200)
            response.headers['Content-Type'] = 'application/json'
            return response
        else:
            response = make_response(json.dumps(
                "Mobile number not Verified, Retry"), 200)
            response.headers['Content-Type'] = 'application/json'
            return response
    else:
        return render_template("verify.html")
