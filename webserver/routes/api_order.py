from flask_restful import Resource
from webserver.entities import OrderManager
from webserver.auth import requires_auth


class ApiOrder(Resource):
    @requires_auth
    def get(self):
        order = OrderManager.get_order()
        print('/api/order: {}'.format(order.as_dict()))
        return order.serialize()
