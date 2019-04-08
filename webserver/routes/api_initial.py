from flask_restful import Resource
from flask import session
from webserver.auth import requires_auth, authenticate
from webserver.storage import Storage
from webserver.entities import User, OrderManager


class ApiInitialData(Resource):
    @requires_auth
    def get(self):
        user = User(session["username"])
        Storage.load_to(user)
        if user.get_id() is None:
            return authenticate()
        current_order = OrderManager.get_order()
        user_order_info = current_order.get_participant(user)
        user_stage = None if user_order_info is None else user_order_info.get_stage()
        # socketio.emit('TEST', user.firstName, broadcast=True, namespace='/ws')
        return {
            'user': user.as_dict(),
            'userStage': user_stage
        }
