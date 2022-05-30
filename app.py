import os
from flask import Flask, render_template, request, redirect, flash, session
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