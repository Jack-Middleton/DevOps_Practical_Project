from application import app
import requests
from flask import render_template, url_for

# nd_stats is shorthand for non dependant, much like d_stats is for dependant

@app.route('/')
def index():
    personal = requests.get('http://personal-api:5000/get-personal-info')
    nd_stats = requests.get('http://nd_stats-api:5000/get-nondependant-stats')
    d_stats = requests.post('http://d_stats-api:5000/get-dependant-stats', json=dict(height=personal.json()['height'], weight=personal.json()['weight'],\
         position= personal.json()['position']))
    return render_template('index.html', personal_stats=personal.json(), non_dependant=nd_stats.json(), dependant=d_stats.json())

