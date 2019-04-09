from flask import render_template, Blueprint
from webserver.auth import requires_auth, do_the_logout

main_bp = Blueprint('main', __name__)


@main_bp.route("/")
@requires_auth
def index():
    return render_template('index.html')


@main_bp.route("/login")
def login():
    do_the_logout()
    return render_template('login.html')
