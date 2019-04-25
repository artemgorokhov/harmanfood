from flask import g
from flask_restful import Resource, reqparse
from webserver.auth import requires_auth, authenticate
import webserver.storage as storage_helper
from webserver.entities import OrderManager, User


class ApiParticipate(Resource):
    @requires_auth
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("the_answer", type=bool, help="Participate in dinner?")
        payload = parser.parse_args()
        i_am_in = payload.get("the_answer", False)
        if i_am_in:
            user = User(g.current_user)
            storage = storage_helper.get_storage()
            storage.load_to(user)
            if user.get_id() is None:
                return authenticate()
            participant = OrderManager.add_participant(user)
            if not participant:
                return {
                    'participate': False,
                    'reason': 'Order is done'
                }
            return {
                'participate': True,
                'initial_stage': str(participant['phase']),
                'initial_food': participant['food'],
                'initial_restaurant': participant['restaurant']
            }
        else:
            return {
                'participate': False,
                'reason': 'Its your choice...'
            }
