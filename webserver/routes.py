from webserver import app
from flask import Flask, render_template, redirect, url_for, send_from_directory
from flask import jsonify, request, session
from webserver.auth import requires_auth, do_the_login, do_the_logout
import os


@app.route("/api/login", methods = ["POST"])
def login_request():
    if request.method == "POST":
        payload = request.get_json()
        username = payload.get("username", "")
        password = payload.get("password", "")
        if do_the_login(username, password):
            resp = jsonify(result = 'success')
            return resp
        else:
            eresp = jsonify(result = 'error')
            return eresp


@app.route("/login", methods = ["GET"])
def login():
    do_the_logout()
    return render_template('login.html')


@app.route("/")
@requires_auth
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 
                            'favicon.png', mimetype='image/vnd.microsoft.icon')
