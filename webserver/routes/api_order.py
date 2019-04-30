from flask import g
from flask_restful import Resource
from webserver.entities import OrderManager
from webserver.auth import requires_auth


class ApiOrder(Resource):
    @requires_auth
    def get(self):
        order = OrderManager.get_order()
        serialized_order = order.serialize(g.current_user)
        print('/api/order: {}'.format(serialized_order))
        return serialized_order
