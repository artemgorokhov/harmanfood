from flask import g
from flask_restful import Resource, reqparse, abort
import webserver.storage as storage_helper
from webserver.entities import Food, OrderManager, User
from webserver.auth import requires_auth


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
        parser.add_argument("dinner", action="append", help="List of dishes for dinner")
        payload = parser.parse_args()
        dinner = payload.get("dinner", None)
        if dinner is None:
            abort(403, error_message="Dishes list is required")
        order = OrderManager.get_order()
        user = User(g.current_user)
        order.update_participant_dinner(user, dinner)
        storage = storage_helper.get_storage()
        storage.save(order)
