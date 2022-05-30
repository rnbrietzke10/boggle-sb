import os
from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from boggle import Boggle


boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return "<h1>Boggle</h1>"