from flask import Flask, redirect, url_for, send_from_directory
import os

app = Flask(__name__, static_folder='../client/')


@app.route("/")
def index():
    if True:
        return redirect(url_for('login'))
    return app.send_static_file('index.html')

@app.route("/login")
def login():
    # return send_from_directory('login', 'login.html')
    return send_from_directory(os.path.join(app.static_folder, 'login'), 'login.html')
