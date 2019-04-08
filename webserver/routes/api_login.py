from flask import Response, render_template
from flask_restful import Resource, reqparse
from webserver.auth import do_the_login, do_the_logout, authenticate


class ApiLogin(Resource):
    def get(self):
        do_the_logout()
        return render_template('login.html')

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help="User name")
        parser.add_argument("password", type=str, help="User password")
        payload = parser.parse_args()
        username = payload.get("username", "").lower()
        password = payload.get("password", "")
        if do_the_login(username, password):
            return Response('Success', 200)
        else:
            err_resp = authenticate()
            return err_resp
