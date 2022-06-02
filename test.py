from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def test_home_route(self):
        """Test home page for status code and ceratin HTML"""
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Boggle</h1>', html)
    
    # def test_user_word_check(self):
    #     with app.test_client() as client:
    #         resp = client.post('/user-word', data={'result': 'ok'})
    #         self.assertEqual(resp.status_code, 204)