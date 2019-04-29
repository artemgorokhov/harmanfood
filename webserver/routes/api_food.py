from flask import g
from flask_restful import Resource, reqparse, abort
import webserver.storage as storage_helper
from webserver.entities import Food, OrderManager, User
from webserver.auth import requires_auth


def create_dinner(payload):
    food_list = payload.get("food_list", None)
    restaurant = payload.get("restaurant", None)
    provider = payload("provider", None)
    if food_list is None or restaurant is None or provider is None:
        abort(403, error_message="Dishes list is required")
    return {
        "food_list": food_list,
        "restaurant": restaurant,
        "provider": provider
    }


class ApiFood(Resource):
    @requires_auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str, help="Restaurant title")
        parser.add_argument("provider", type=str, help="Food provider")
        payload = parser.parse_args()
        restaurant_title = payload.get("title", None)
        provider = payload.get("provider", None)
        if not restaurant_title or not provider:
            abort(403, error_message="Restaurant title and provider name are required")
        storage = storage_helper.get_storage()
        food_list = storage.find(Food, {"provider": provider, "restaurant": restaurant_title})
        return {
            'food': food_list
        }

    @requires_auth
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("food_list", action="append", help="List of dishes for dinner")
        parser.add_argument("restaurant", type=str, help="Restaurant for dinner")
        parser.add_argument("provider", type=str, help="Rest provider")
        payload = parser.parse_args()
        status = OrderManager.update_participant_dinner(g.current_user, create_dinner(payload))
        if not status:
            abort(403, error_message="Order was not updated")
        return {
            'status': 'success'
        }
