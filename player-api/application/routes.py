from application import app
from flask import jsonify, request
from random import randint


@app.route('/jumping-reach', methods=['POST'])
def jumping_reach():
    request_data = request.get_json()
    personal = request_data['height']
    if personal < 170:
        cap = 13
    elif personal < 190:
        cap = 15
    elif personal < 210:
        cap = 17
    else:
        cap = 20
    jumping = randint(1, cap)
    return jsonify(jumping=jumping)