from webserver import app
from flask import render_template, send_from_directory
from webserver.auth import requires_auth, do_the_logout


@app.route("/login", methods=["GET"])
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
                               'favicon.png',
                               mimetype='image/vnd.microsoft.icon')
