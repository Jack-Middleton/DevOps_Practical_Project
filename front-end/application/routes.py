from application import app
import requests

# nd_stats is shorthand for non dependant

@app.route('/')
def index():
    personal = requests.get('http://personal-api:5000/get-personal-info')
    nd_stats = requests.get('http://nd_stats-api:5000/get-nondependant-stats')
    jumping = requests.post('http://d_stats-api:5000/dependant-stats', json=dict(height=personal.json()['height'], weight=['weight'], position= ['position']))
    return f'{personal.json()} | {nd_stats.json()} | {jumping.json()}'
