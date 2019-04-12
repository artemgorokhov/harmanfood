from flask import g
from flask_restful import Resource
from webserver.auth import requires_auth, authenticate
import webserver.storage as storage_helper
from webserver.entities import User, OrderManager
from webserver.entities.order_state import NotStartedState


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
        print('USER ORDER: {}'.format(user_order_info))
        user_stage = NotStartedState() if not user_order_info else user_order_info['stage']
        # socketio.emit('TEST', user.firstName, broadcast=True, namespace='/ws')
        return {
            'user': user.as_dict(),
            'userStage': str(user_stage),
            'orderIsDone': current_order.is_done()
        }
