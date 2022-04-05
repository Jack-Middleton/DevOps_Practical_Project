from flask import url_for
from flask_testing import TestCase
import pytest
import requests_mock
from application import app
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestFrontend(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as m:
            m.get('http://personal-api:5000/get-personal-info', json={'height':165, 'weight':75, 'position':'GK' })
            m.get('http://nd_stats-api:5000/get-nondependant-stats', json={'first_touch':13})
            m.post('http://d_stats-api:5000/get-dependant-stats', json={'marking':13})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'height : 165', response.data)
            self.assertIn(b'first_touch : 13', response.data)
            self.assertIn(b'marking : 13', response.data)
