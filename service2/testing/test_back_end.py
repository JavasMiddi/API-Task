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
    def test_animalpage_view(self):
        response = self.client.get(url_for('animal_name'))
        self.assertEqual(response.status_code, 200)
   
    def test_noisepage_view(self):
        response = self.client.post(url_for('animal_noise'))
        self.assertEqual(response.status_code, 200)
   
    def test_noisepage_cat(self):
        response = self.client.post(url_for('animal_noise'), data="cat")
        self.assertIn(b'meow', response.data)

    def test_noisepage_dog(self):
        response = self.client.post(url_for('animal_noise'), data="dog")
        self.assertIn(b'woof', response.data)

    def test_noisepage_cow(self):
        response = self.client.post(url_for('animal_noise'), data="cow")
        self.assertIn(b'moo', response.data)

    def test_noisepage_duck(self):
        response = self.client.post(url_for('animal_noise'), data="duck")
        self.assertIn(b'quack', response.data)

