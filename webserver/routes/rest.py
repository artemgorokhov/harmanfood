from flask import request, jsonify, Response, session
from webserver import app, socketio
from webserver.auth import do_the_login, authenticate, requires_auth
from webserver.entities import User, Restaurant, OrderManager
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
        current_order = OrderManager.get_order()
        user_order_info = current_order.get_participant(user)
        user_stage = None if user_order_info is None else user_order_info.get_stage()
        socketio.emit('TEST', user.firstName, broadcast=True, namespace='/ws')
        return jsonify(user=user.as_dict(),
                       userStage=user_stage)


@app.route("/api/restaurant_list", methods=["POST"])
@requires_auth
def restaurant_request():
    if request.method == "POST":
        rest_list = Storage.find(Restaurant)
        return jsonify(restaurants=rest_list)
