from flask import render_template, Blueprint
from webserver.auth import requires_auth

main_bp = Blueprint('main', __name__)


@main_bp.route("/")
@requires_auth
def index():
    return render_template('index.html')
