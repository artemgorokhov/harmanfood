from flask import g
from flask_restful import Resource
from webserver.auth import requires_auth, authenticate
import webserver.storage as storage_helper
from webserver.entities import User, OrderManager


class ApiInitialData(Resource):
    @requires_auth
    def get(self):
        user = User(g.current_user)
        storage = storage_helper.get_storage()
        storage.load_to(user)
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
