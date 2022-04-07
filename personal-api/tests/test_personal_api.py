from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
from application import app
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestPersonal(TestBase):
    def test_name(self):
        with patch('application.routes.choice') as r:
            r.return_value='Jeremy'
            response = self.client.get(url_for('get_name'))
            self.assert200(response)
            self.assertIn(b'Jeremy', response.data)
