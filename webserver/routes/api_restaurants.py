from flask_restful import Resource
import webserver.storage as storage_helper
from webserver.entities import Restaurant
from webserver.auth import requires_auth


class ApiRestaurant(Resource):
    @requires_auth
    def get(self):
        storage = storage_helper.get_storage()
        rest_list = storage.find(Restaurant)
        return rest_list
