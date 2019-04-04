from flask import request, jsonify, Response, session
from webserver import app
from webserver.auth import do_the_login, authenticate, requires_auth
from webserver.entities import User, Restaurant
from webserver.storage import Storage


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


@app.route("/api/initial_data", methods=["POST"])
@requires_auth
def initial_request():
    if request.method == "POST":
        user = User(session["username"])
        Storage.load_to(user)
        if user.get_id() is None:
            return authenticate()
        # restaurants = Storage.find(Restaurant)
        # return jsonify(user=user,
        # 			   restaurants=restaurants)
        return jsonify(user=user.as_dict(),
                       patron=user.as_dict())


@app.route("/api/restaurant_list", methods=["POST"])
@requires_auth
def restaurant_request():
    if request.method == "POST":
        rest_list = Storage.find(Restaurant)
        return jsonify(restaurants=rest_list)
