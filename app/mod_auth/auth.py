import json
import re
import datetime
from flask import (Blueprint, render_template, request, make_response)

from app.models.models import User
from app.models.session import session

mod_auth = Blueprint('auth', __name__)

@mod_auth.route('/sms_verification', methods=['GET','POST'])
def sms_verification():
    if request.method == 'POST':
        mobile_no = request.form.get('mobile')