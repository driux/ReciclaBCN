import os
from app import app
from flask import render_template
'''
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
'''

@app.route('/')
def template_test():
    return render_template('index.html', name="Luigi")
