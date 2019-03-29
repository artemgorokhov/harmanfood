from functools import wraps
from flask import Response, redirect, url_for
from flask import session
from webserver.storage import Storage
from webserver.entities import User


def do_the_login(username, password):
    if not check_auth(username, password):
        return False
    session["username"] = username
    return True


def do_the_logout():
    session.pop("username", None)


def check_auth(username, password):
    print("Checking auth for user {}".format(username))
    user = User(username)
    Storage.load_to(user)
    if user.get_id() is None:
        print("There is no user {} in database".format(username))
        return False
    if user.password_to_be_reset(password):
        Storage.save(user)
        return True
    if not user.verify_password(password):
        print("Wrong password for user {}".format(username))
        return False
    return True


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("username"):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated
