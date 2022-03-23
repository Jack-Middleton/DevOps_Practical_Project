from application import app
from flask import jsonify
from random import choice, randint

first_names = ['James', 'Jeremy', 'Bob', 'Matt', 'Jimmy', 'Ed', 'Arthur', 'Steven']
last_names = ['Irons', 'Bobsworth', 'Doe', 'Smith', 'Jimsworth']
positions = ['GK', 'LCB', 'RCB', 'LB', 'RB', 'DM', 'CM', 'RM', 'LM', 'CAM', 'LAM', 'RAM', 'LW', 'RW', 'STR']
nationalities = ['English', 'Irish', 'Scottish', 'Welsh']
preferred_foot = ['Left', 'Right']



@app.route('/get-personal-info', methods=['GET'])
def get_name():
    # create a random name from the first and last name lists 
    f_name = choice(first_names)
    l_name = choice(last_names)
    name = str(f_name + " " + l_name)

    # generate a random height in cm
    height = randint(150, 220)

    # generate a random weight in kg
    weight = randint(55, 105)

    # generate a random position
    position = choice(positions)

    # generate a random nationality
    nationality = choice(nationalities)

    # pick a preferred foot
    pref_foot = choice(preferred_foot)

    # returns the information for the front-end / other routes to work with
    return jsonify(name=name, height=height, weight=weight, position=position, naitonality=nationality, pref_foot = pref_foot)



