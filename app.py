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
    board = boggle_game.make_board()
    session['board'] = board

    return render_template('home.html', board = session['board'])

@app.route('/user-word', methods=['POST'])
def user_word_check():
    word = request.get_json()['word']
    valid_word = boggle_game.check_valid_word(session['board'], word)
    return_data = {'result': valid_word}

    return jsonify(return_data)

@app.route('/player-data', methods=['POST'])
def player_data():
    session['board'] = boggle_game.make_board()
    player_info = request.get_json()
    print(player_info)
    return redirect('/')