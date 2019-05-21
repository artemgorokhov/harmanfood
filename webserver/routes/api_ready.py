from flask_restful import Resource
from webserver.auth import requires_auth


class ApiReady(Resource):
    @requires_auth
    def post(self):
        return {
            'userstage': 'Delivery'
        }
