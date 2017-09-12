import json
import re
import datetime
from flask import (Blueprint, render_template, request, make_response)

from app.models.session import session
from app.helpers.helpers import send_confirmation_code, create_mobile_user

mod_auth = Blueprint('auth', __name__)


@mod_auth.route('/sms_verification', methods=['GET','POST'])
def sms_verification():
    if request.method == 'POST':
        mobile_no = request.form.get('mobile')
        if re.match(r'[789]\d{9}$', to_number):
            new_user = create_mobile_user(mobile_no)
            send_confirmation_code(new_user.mobile_no, new_user.otp)
            response = make_response(json.dumps(
                "OTP sent to your Mobile Number"), 200)
            response.headers['Content-Type'] = 'application/json'
            return response

    else:
        return render_template("main.html")


@mod_auth.route('/mobile_otp_verification', methods=['GET', 'POST'])
def verify_user():
