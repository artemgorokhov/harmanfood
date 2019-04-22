from flask_restful import Resource
from webserver.entities.order_manager import OrderManager
from webserver.entities import Restaurant
from webserver.auth import requires_auth


class ApiOrder(Resource):
    @requires_auth
    def get(self):
        order = OrderManager.get_order()
        print('/api/order: {}'.format(order.as_dict()))
        return order.as_dict()
