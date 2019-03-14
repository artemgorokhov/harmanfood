from webserver import app
from flask import Flask, render_template, redirect, url_for, send_from_directory
from webserver.auth import requires_auth
import os

@app.route("/login")
def login():
    # return send_from_directory('login', 'login.html')
    print('Folder: {}'.format(os.path.join(app.static_folder, 'login')))
    return send_from_directory(os.path.join(app.static_folder, 'login'), 'login.html')

@app.route("/")
@requires_auth
def index():
    return render_template('index.html')
