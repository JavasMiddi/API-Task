import requests
import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestViews(TestBase):
    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    def test_generate_view(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "dog"
                p.return_value.text = "woof"
                response = self.client.get(url_for('animal'))
                self.assertIn(b'dog', response.data)
                self.assertIn(b'woof', response.data)
                self.assertEqual(response.status_code, 200)
