from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
from application import app
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class Test_dStats(TestBase):
    def test_height_happy(self):
        with patch('application.routes.randint') as r:
            r.return_value=13
            response = self.client.post(url_for('dependant_stats'), 
            json={'height':165, 'weight':74, 'position':'GK'}) 
            self.assert200(response)
            self.assertIn(b'13', response.data)

    def test_height_f_bad(self):
        with patch('application.routes.randint') as r:
            r.return_value=13
            response = self.client.post(url_for('dependant_stats'), 
            json={'height':175, 'weight':84, 'position':'LB'}) 
            self.assert200(response)
            self.assertIn(b'13', response.data)

    def test_height_s_bad(self):
        with patch('application.routes.randint') as r:
            r.return_value=13
            response = self.client.post(url_for('dependant_stats'), 
            json={'height':205, 'weight':96, 'position':'CM'}) 
            self.assert200(response)
            self.assertIn(b'13', response.data)
    
    def test_height_else(self):
        with patch('application.routes.randint') as r:
            r.return_value=13
            response = self.client.post(url_for('dependant_stats'), 
            json={'height':215, 'weight':96, 'position':'STR'}) 
            self.assert200(response)
            self.assertIn(b'13', response.data)

        