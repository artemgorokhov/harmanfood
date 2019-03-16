from webserver import app
from flask import Flask, render_template, redirect, url_for, send_from_directory
from webserver.auth import requires_auth
import os

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/")
@requires_auth
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 
                            'favicon.png', mimetype='image/vnd.microsoft.icon')
