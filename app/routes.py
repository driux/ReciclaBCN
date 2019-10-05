import os
from app import app
from flask import render_template, request


'''
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
'''

@app.route('/')
def template_test():
    return render_template('index.html', name="Luigi")


@app.route('/punto-verde')
def template_greenpoint():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    print(lat, lon)
    if lat is None or lon is None:
        return render_template('greenpoint-redirect.html');
    else:
        return render_template('greenpoint.html', page_text="Hola");


@app.route('/a-donde-va')
def template_classifier():
    img = request.args.get('img')
    if img is None:
        return render_template('classifier-img.html');
    else:
        return render_template('classifier.html', page_text="Hola");
