from flask import g
import json
from flask_restful import Resource, reqparse, abort
import webserver.storage as storage_helper
from webserver.entities import Food, OrderManager
from webserver.auth import requires_auth


def create_dinner(payload):
    food_list_strings = payload.get("food_list", []) or []
    restaurant = payload.get("restaurant", None)
    provider = payload.get("provider", None)
    if restaurant is None or provider is None:
        abort(403, error_message="Dishes list is required")
    food_list = []
    for dish in food_list_strings:
        dish_acceptable_string = dish.replace("'", "\"")
        food_list.append(json.loads(dish_acceptable_string))
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
        dishes = OrderManager.update_participant_dinner(g.current_user, create_dinner(payload))
        if dishes is None:
            abort(403, error_message="Order was not updated")
        return {
            "dishes": dishes
        }
