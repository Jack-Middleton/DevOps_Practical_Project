from application import app
from flask import jsonify
from random import randint

@app.route('/get-nondependant-stats', methods=['GET'])
def get_nondependant_stats():
    ''' Generates the stats that arent dependant on another value when generating, ie; all mental attributes can be randomly
    generated, as can a handful of technical and a couple of physical attributes, but others are reliant on things such as 
    position, height etc. '''

    # first touch
    f_t = randint(1,20)
    # free kick taking
    fk_t = randint(1,20)
    # passing
    pass_ = randint(1,20)
    # technique
    tech = randint(1,20)
    # aggression
    agg = randint(1,20)
    # anticipation
    ant = randint(1,20)
    # bravery
    brave = randint(1,20)
    # composure
    comp = randint(1,20)
    # concentration
    conc = randint(1,20)
    # decisions
    dec = randint(1,20)
    # determination
    det = randint(1,20)
    # flair
    fla = randint(1,20)
    # leadership
    lead = randint(1,20)
    # off the ball
    otb = randint(1,20)
    # positioning
    pos = randint(1,20)
    # teamwork
    team = randint(1,20)
    # vision
    vis = randint(1,20)
    # workrate
    wr = randint(1,20)
    # natural fitness
    nf = randint(1,20)
    return jsonify(first_touch=f_t, freekick_taking=fk_t, passing=pass_, technique=tech, aggression=agg, \
    anticipation=ant, bravery=brave, composure=comp, concentration=conc, decisions=dec, determination=det, flair=fla, \
    leadership=lead, off_the_ball=otb, positioning=pos, teamwork=team, vision=vis, work_rate=wr, natural_fitness = nf)