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
        return {
            'user': user.as_dict(),
            'orderIsDone': current_order.is_done()
        }
