from application import app
import requests

@app.route('/')
def index():
    personal = requests.get('http://personal-api:5000/get-name')
    stats = requests.get('http://stats-api:5000/get-stats')
    jumping = requests.post('http://player-api:5000/jumping-reach', json=dict(height=personal.json()['height']))
    return f'{personal.json()} | {stats.json()} | {jumping.json()}'
