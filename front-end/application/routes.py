from application import app
import requests

# nd_stats is shorthand for non dependant

@app.route('/')
def index():
    personal = requests.get('http://personal-api:5000/get-name')
    nd_stats = requests.get('http://stats-api:5000/get-nondependant-stats')
    jumping = requests.post('http://player-api:5000/jumping-reach', json=dict(height=personal.json()['height']))
    return f'{personal.json()}'
