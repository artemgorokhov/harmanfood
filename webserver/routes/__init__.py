from .routes import main_bp
from .api_restaurants import ApiRestaurant
from .api_food import ApiFood
from .api_order import ApiOrder
from .api_initial import ApiInitialData
from .api_login import ApiLogin
from .api_participate import ApiParticipate
from .api_ready import ApiReady
from flask import Blueprint
from flask_restful import Api


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(ApiInitialData, "/api/initial_data")
api.add_resource(ApiRestaurant, "/api/restaurant_list")
api.add_resource(ApiLogin, "/api/login")
api.add_resource(ApiParticipate, "/api/participate")
api.add_resource(ApiFood, "/api/menu")
api.add_resource(ApiOrder, "/api/order")
api.add_resource(ApiReady, "/api/ready")
