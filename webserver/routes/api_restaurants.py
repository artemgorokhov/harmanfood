from flask_restful import Resource
import webserver.storage as storage_helper
from webserver.entities import Restaurant
from webserver.auth import requires_auth


class ApiRestaurant(Resource):
    @requires_auth
    def get(self):
        storage = storage_helper.get_storage()
        rest_list = storage.find(Restaurant)
        print("/api/restaurant_list: {}".format(rest_list))
        return {
            'restaurants': rest_list
        }
