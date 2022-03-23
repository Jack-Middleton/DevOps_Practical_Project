from application import app
from flask import jsonify
from random import randint

@app.route('/get-stats', methods=['GET'])
def get_stats():
    pace = randint(1,20)
    strength = randint(1,20)
    stats = dict(pace=pace, strength=strength)
    return jsonify(stats=stats)