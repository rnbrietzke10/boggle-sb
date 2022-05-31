import os
import json
from flask import Flask, render_template, request, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from boggle import Boggle


boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

board = boggle_game.make_board()

@app.route('/')
def home_page():
    """
    boggle_game.make_board() returns:
    [
        ['W', 'X', 'Y', 'C', 'R'],
        ['W', 'P', 'B', 'L', 'U'],
        ['Z', 'K', 'V', 'S', 'C'],
        ['W', 'D', 'X', 'T', 'H'],
        ['Z', 'X', 'Z', 'J', 'T']
    ]
    """
    session['board'] = board

    return render_template('home.html', board = session['board'])

@app.route('/user-word', methods=['POST'])
def user_word_check():
    # print(type(request.data))
    # print(request.get_json()['word'])
    # dict_data = request.data.decode()
    word = request.get_json()['word']
    valid_word = boggle_game.check_valid_word(session['board'], word)
    return_data = {'result': valid_word}

    return jsonify(return_data)