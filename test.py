from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    def setUp(self):
        """Stuff to do before every test."""
        self.client = app.test_client()
        app.config['TESTING'] = True


    # TODO -- write tests for every view function / feature!
    def test_home_route(self):
        """Test home page for status code and ceratin HTML"""
        with self.client:
            resp = self.client.get('/')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Boggle</h1>', html)

    def test_user_word_check(self):
        """Test if word is vaild and on the board"""
        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["H", "E", "L", "L", "O"],
                                 ["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"]]
        resp = self.client.get('/user-word?word=hello')
        self.assertEqual(resp.json['result'], 'ok')