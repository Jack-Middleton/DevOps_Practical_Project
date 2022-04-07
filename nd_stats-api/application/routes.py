from application import app
from flask import jsonify
from random import randint

@app.route('/get-nondependant-stats', methods=['GET'])
def get_nondependant_stats():
    ''' Generates the stats that arent dependant on another value when generating, ie; all mental attributes can be randomly
    generated, as can a handful of technical and a couple of physical attributes, but others are reliant on things such as 
    position, height etc. '''

    non_dependant = ['first_touch', 'freekick_taking', 'passing', 'technique', 'aggression', 'anticipation', 'bravery', 'composure', \
    'concentration', 'decisions', 'determination', 'flair', 'leadership', 'off_the_ball', 'positioning', 'teamwork', 'vision', \
    'work_rate', 'natural_fitness']
    for stat in non_dependant:
        globals()[stat]=randint(1,20)

    
    return jsonify(first_touch=first_touch, freekick_taking=freekick_taking, passing=passing, technique=technique, aggression=aggression, \
    anticipation=anticipation, bravery=bravery, composure=composure, concentration=concentration, decisions=decisions, determination=determination, flair=flair, \
    leadership=leadership, off_the_ball=off_the_ball, positioning=positioning, teamwork=teamwork, vision=vision, work_rate=work_rate, natural_fitness = natural_fitness)