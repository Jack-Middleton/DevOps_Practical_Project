from application import app
from flask import jsonify
from random import choice, randint

first_names = ['James', 'Jeremy', 'Bob', 'Matt', 'Jimmy', 'Ed', 'Arthur', 'Steven']
last_names = ['Irons', 'Bobsworth', 'Doe', 'Smith', 'Jimsworth']


@app.route('/get-name', methods=['GET'])
def get_name():
    f_name = choice(first_names)
    l_name = choice(last_names)
    name = str(f_name + " " + l_name)
    height = randint(150, 220)

    return jsonify(name=name, height=height)






# below is the basic syntax for get, post, put, patch and delete requests

# people = [{'name': 'John Doe', 'age': '19'}, {'name': 'James Doe', 'age': '23'}]

# @app.route('/get/<int:index>', methods=['GET'])
# def get(index):
#     if index - 1 < len(people):
#         person = people[index -1 ]
#         return jsonify(person)
#     return jsonify(message='Not Found', status=404), 404

# @app.route('/post')
# def post():
#     data = request.get_json()
#     people.append(data)
#     return jsonify(message='Person added', status=200), 200

# @app.route('/put/<int:index>', methods=['PUT'])
# def put(index):
#     if index - 1 < len(people):
#         people[index-1] = request.get_json()
#         return jsonify(message="Updated Person")
#     return jsonify(message='Not Found', status=404), 404

# @app.route('/patch/<int:index>', methods=['PATCH'])
# def patch(index):
#     if index - 1 < len(people):
#         data = request.get_json()
#         for k, v in data.items():
#             people[index - 1][k] = v
#         return jsonify(message='Updated Person')
#     return jsonify(message='Not Found', status=404), 404


# @app.route('/delete/<int:index>', methods=['DELETE'])
# def delete(index):
#     if index - 1 < len(people):
#         people.pop(index-1)
#         return jsonify(message='Person deleted')
#     return jsonify(message='Not Found', status=404), 404