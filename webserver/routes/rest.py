from flask import request, jsonify
from webserver import app
from webserver.auth import do_the_login


@app.route("/api/login", methods=["POST"])
def login_request():
    if request.method == "POST":
        payload = request.get_json()
        username = payload.get("username", "").lower()
        password = payload.get("password", "")
        if do_the_login(username, password):
            resp = jsonify(result='success')
            return resp
        else:
            err_resp = jsonify(result='error')
            return err_resp
