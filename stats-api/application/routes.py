from application import app
from flask import jsonify
from random import randint

@app.route('/get-nondependant-stats', methods=['GET'])
def get_nondependant_stats():
    ''' Generates the stats that arent dependant on another value when generating, ie; all mental attributes can be randomly
    generated, as can a handful of technical and a couple of physical attributes, but others are reliant on things such as 
    position, height etc. '''


    return jsonify()