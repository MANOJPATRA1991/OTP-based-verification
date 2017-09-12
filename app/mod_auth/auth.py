import json
import re
import datetime
from flask import (Blueprint, render_template, request, make_response)
from app.models.models import User
from app.models.session import session
from app.helpers.helpers import generate_code, send_confirmation_code, create_mobile_user

mod_auth = Blueprint('auth', __name__)


@mod_auth.route('/sms_verification', methods=['GET','POST'])
def sms_verification():
    if request.method == 'POST':
        mobile_no = request.form.get('mobile')
        if not re.match(r'[789]\d{9}$', mobile_no):
            response = make_response(json.dumps('Invalid mobile number!'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response
        else:
            user = session.query(User).filter_by(mobile_no=mobile_no).first()
            if user is not None and user.is_verified:
                response = make_response(json.dumps(
                    "Mobile number is already verified."), 200)
                response.headers['Content-Type'] = 'application/json'
                return response
            if user is None:
                new_user = create_mobile_user(mobile_no)
                session.add(new_user)
                session.commit()
                print(new_user)
                send_confirmation_code(new_user.mobile_no, new_user.otp)
            elif user is not None and not user.is_verified:
                user.otp = generate_code()
                session.add(user)
                session.commit()
                send_confirmation_code(user.mobile_no, user.otp)
            response = make_response(json.dumps(
                "OTP sent to your Mobile Number"), 200)
            response.headers['Content-Type'] = 'application/json'
            return response
    else:
        return render_template("main.html")


@mod_auth.route('/mobile_otp_verification', methods=['GET', 'POST'])
def verify_user():
    if request.method == 'POST':
        mobile_no = request.args.get('mobile')
        otp = request.args.get('otp')
        user = session.query(User).filter_by(mobile_no=mobile_no).first()
        if user is not None and not user.is_verified:
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
                print("A")
                response = make_response(json.dumps(
                    "Mobile number not Verified, Retry"), 200)
                response.headers['Content-Type'] = 'application/json'
                return response
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
