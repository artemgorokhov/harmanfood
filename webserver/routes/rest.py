from flask import request, jsonify, Response
from webserver import app
from webserver.auth import do_the_login, authenticate


@app.route("/api/login", methods=["POST"])
def login_request():
    if request.method == "POST":
        payload = request.get_json()
        username = payload.get("username", "").lower()
        password = payload.get("password", "")
        if do_the_login(username, password):
            return Response('Success', 200)
        else:
            err_resp = authenticate()
            return err_resp
