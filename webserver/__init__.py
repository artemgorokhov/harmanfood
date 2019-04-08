import os
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from webserver.storage import Storage
from config import config

# TODO: implement storage management
# db = Storage()

socketio = SocketIO()


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')
    app = Flask(__name__,
                static_folder='../dist/static',
                template_folder='../dist')
    app.config.from_object(config[config_name])

    socketio.init_app(app)

    # Register routes
    from webserver import routes
    app.register_blueprint(routes.main_bp)
    app.register_blueprint(routes.api_bp)

    if config_name == 'development':
        # CORS enabled only for development at the moment
        CORS(app)

    return app
