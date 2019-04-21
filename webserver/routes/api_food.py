from flask_restful import Resource, reqparse, abort
import webserver.storage as storage_helper
from webserver.entities import Food
from webserver.auth import requires_auth


class ApiFood(Resource):
    @requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("restaurant", type=str, help="Restaurant title")
        parser.add_argument("provider", type=str, help="Food provider")
        payload = parser.parse_args()
        restaurant_title = payload.get("restaurant", None)
        provider = payload.get("provider", None)
        if not restaurant_title or not provider:
            abort(403, error_message="Restaurant title and provider name are required")
        storage = storage_helper.get_storage()
        food_list = storage.find(Food, {"provider": provider, "restaurant": restaurant_title})
        return food_list
