import json

from flask import Flask, abort, request
from flask.json import jsonify

from .expandi import go_high

app = Flask(__name__)

@app.route('/test-data', methods=['POST'])
def webhook():
    if request.method == 'POST':
        try:
            data = request.json
            email = data.get('contact').get('email')
            go_high.contact_lookup(email=email)
            return {
                "message":"Email Received Successfully",
                "email":email
            }
        except Exception as e:
            return {
                "message":"Email not Received Successfully",
                "errors":jsonify(e)
            }
    else:
        abort(400)

