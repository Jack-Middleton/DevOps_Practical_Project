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
    
    physical_stats = {'acceleration':[speed_base, speed_cap], 'agility':[speed_base, speed_cap], 'balance':[physical_base, physical_cap], \
    'pace':[speed_base, speed_cap], 'stamina':[physical_base, physical_cap], 'strength':[physical_base, physical_cap]}
    for k,v in physical_stats.items():
        globals()[k]=randint(v[0], v[1])

    # check if position is goalkeeper first, if so, determine GK stats
    # otherwise, use position to determine caps for other stats
    position = request_data['position']

    # setting GK stats to False, to use as a boolean check later to determine which set of stats to return
    GK_stats = False
    if position == 'GK':
        GK_stats = True
        gk_stats = ['aerial_reach', 'command_of_area','communication', 'eccentricity', 'first_touch', 'handling', 'kicking', 'one_on_ones', 'punching', \
        'reflexes', 'rushing_out', 'throwing']
        for stat in gk_stats:
            globals()[stat]=randint(1,20)

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
    outfield = {'corners': mid_base, 'crossing':mid_base,'dribbling': str_base, 'finishing': str_base, 'heading': 1, 'long_shots': mid_base, 'long_throws': 1,\
         'marking': def_base, 'tackling': def_base}
    for k,v in outfield.items():
        globals()[k]=randint(v,20)

    if GK_stats:
        return jsonify(jumping_reach=jumping, acceleration=acceleration, agility=agility, balance=balance, pace=pace, stamina=stamina, strength=strength, \
        aerial_reach=aerial_reach, command_of_area=command_of_area,communication=communication, eccentricity=eccentricity, first_touch=first_touch,\
             handling=handling, kicking=kicking, \
        one_on_ones=one_on_ones, punching_tendency=punching, reflexes=reflexes, rushing_out_tendency=rushing_out, throwing=throwing)
    else:
        return jsonify(jumping_reach=jumping, acceleration=acceleration, agility=agility, balance=balance, pace=pace, stamina=stamina, strength=strength, \
        corners=corners, crossing=crossing, dribbling=dribbling, finishing=finishing, heading=heading, long_shots=long_shots, long_throws=long_throws,\
             marking=marking, tackling=tackling)

