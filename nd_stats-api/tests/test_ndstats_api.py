from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
from application import app
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app


class Test_ndStats(TestBase):
    def test_dstats(self):
        with patch('application.routes.randint') as r:
            r.return_value = 13
            response = self.client.get(url_for('get_nondependant_stats'))
            self.assert200(response)
            self.assertIn(b'13', response.data)