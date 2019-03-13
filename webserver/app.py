from flask import Flask, render_template, redirect, url_for, send_from_directory
import os

app = Flask(__name__, 
            static_folder='../dist/static',
            template_folder='../dist')


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    # return send_from_directory('login', 'login.html')
    return send_from_directory(os.path.join(app.static_folder, 'login'), 'login.html')
