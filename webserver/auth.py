from webserver import app
from functools import wraps
from flask import request, Response, redirect, url_for, render_template
from flask import session


def do_the_login(username, password):
    if not check_auth(username, password):
        return False
    session["username"] = username
    return True


def do_the_logout():
    session.pop("username", None)


def check_auth(username, password):
    '''
    Implement this function when choose database
    '''
    return username == 'admin' and password == 'pass'


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("username"):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated
