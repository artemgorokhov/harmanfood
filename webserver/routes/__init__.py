from . import routes, ws
from .api_restaurants import ApiRestaurant
from .api_initial import ApiInitialData
from .api_login import ApiLogin
from webserver import app
from flask_restful import Api

api = Api(app)

api.add_resource(ApiInitialData, "/api/initial_data")
api.add_resource(ApiRestaurant, "/api/restaurant_list")
api.add_resource(ApiLogin, "/api/login")
