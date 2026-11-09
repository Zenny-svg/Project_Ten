# app.py
from flask import Flask, request, render_template
from markupsafe import Markup
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', my_name="Zoe", my_fact="I love sleeping during rainstorms.")

@app.route('/about')
def about():
    return render_template('about.html', goal_1 = "My first goal is to learn Python.", goal_2 = "My second goal is to learn how to make a website.", goal_3 = "My third goal is to get at least a B in this course.")

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)
