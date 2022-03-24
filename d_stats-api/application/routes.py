from application import app
from flask import jsonify, request
from random import randint



@app.route('/get-dependant-stats', methods=['POST'])
def dependant_stats():
    speed_cap = 20
    speed_base = 1
    physical_cap = 20
    physical_base = 1
    def_base = 1
    str_base = 1
    mid_base = 1
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

    # check if position is goalkeeper first, if so, determine GK stats
    # otherwise, use position to determine caps for other stats
    position = request_data['position']

    # setting GK stats to False, to use as a boolean check later to determine which set of stats to return
    GK_stats = False
    if position == 'GK':
        GK_stats = True
        # Aerial Reach
        aer = randint(1,20)
        # Command of Area
        coa = randint(1,20)
        # Communication
        comm = randint(1,20)
        # Eccentricity
        ecc = randint(1,20)
        # First Touch
        ft = randint(1,20)
        # Handling
        hand = randint(1,20)
        # Kicking
        kick = randint(1,20)
        # One on Ones
        one = randint(1,20)
        # Punching (tendency)
        punch = randint(1,20)
        # Reflexes
        ref = randint(1,20)
        # Rushing Out (tendency)
        rush = randint(1,20)
        # Throwing
        throw = randint(1,20)
    elif 'B' in position:
        # confirms that the player is one of the defensive positions
        # will likely have a higher base tackling & marking
        def_base = 9
    elif 'M' in position:
        # player is a midfielder, higher corners, crossing, long shots
        # but they also will have decent forward abilities
        mid_base = 9
        str_base = 6
    else: 
        # player is a striker or winger, higher dribbling, finishing, but will also have decent corners and crossing
        str_base = 9
        mid_base = 6

    # now that the caps are determined, another round of randomly generated stats
    # corners
    cor = randint(mid_base, 20)
    # crossing
    cross = randint(mid_base, 20)
    # dribbling
    drib = randint(str_base, 20)
    # finishing
    fin = randint(str_base, 20)
    # heading 
    head = randint(1,20)
    # long shots
    long = randint(mid_base, 20)
    # long throws 
    long_t = randint(1,20)
    # marking
    mark = randint(def_base, 20)
    # tackling
    tack = randint(def_base, 20)

    if GK_stats:
        return jsonify(jumping_reach=jumping, acceleration=acc, agility=agi, balance=bal, pace=pac, stamina=sta, strength=str_, \
        aerial_reach=aer, command_of_area=coa,communication=comm, eccentricity=ecc, first_touch=ft, handling=hand, kicking=kick, \
        one_on_ones=one, punching_tendency=punch, reflexes=ref, rushing_out_tendency=rush, throwing=throw)
    else:
        return jsonify(jumping_reach=jumping, acceleration=acc, agility=agi, balance=bal, pace=pac, stamina=sta, strength=str_, \
        corners=cor, crossing=cross, dribbling=drib, finishing=fin, heading=head, long_shots=long, long_throws=long_t, marking=mark, tackling=tack)

