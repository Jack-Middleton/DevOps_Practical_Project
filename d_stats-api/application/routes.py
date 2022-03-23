from application import app
from flask import jsonify, request
from random import randint


@app.route('/dependant-stats', methods=['POST'])
def dependant_stats():

    # determine the jumping reach, which is dependant on height
    request_data = request.get_json()
    height = request_data['height']
    if height < 170:
        cap = 13
    elif height < 190:
        cap = 15
    elif height < 210:
        cap = 17
    else:
        cap = 20
    jumping = randint(1, cap)
   

    # determine base and caps for physical attribute generation
    weight = request_data['weight']
    if weight < 75:
        speed_cap = 20
        speed_base = 10
        physical_cap = 13
        physical_base = 3
    elif weight < 95:
        speed_cap = 15
        speed_base = 7
        physical_cap = 15
        physical_base = 7
    else: 
        speed_cap = 13
        speed_base = 3
        physical_cap = 20
        physical_base = 10
    
    # acceleration
    acc = randint(speed_base, speed_cap)
    # agility
    agi = randint(speed_base, speed_cap)
    # balance
    bal = randint(physical_base, physical_cap)
    # pace
    pac = randint(speed_base, speed_cap)
    # stamina
    sta = randint(physical_base, physical_cap)
    # strength
    str_ = randint(physical_base, physical_cap)




    return jsonify(jumping_reach=jumping, acceleration=acc, agility=agi, balance=bal, pace=pac, stamina=sta, strength=str_)
