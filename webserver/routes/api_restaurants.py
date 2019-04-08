from flask_restful import Resource
from webserver.storage import Storage
from webserver.entities import Restaurant
from webserver.auth import requires_auth


class ApiRestaurant(Resource):
    @requires_auth
    def get(self):
        rest_list = Storage.find(Restaurant)
        return rest_list
