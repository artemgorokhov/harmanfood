import os
from pymongo import MongoClient
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from config import config

# Extensions
db_client = MongoClient()
db = db_client.harmanfood
socketio = SocketIO()


def emit_order(serialized_order):
    print("SOCKETIO: Emitting changed order {}".format(serialized_order))
    socketio.emit('ORDER', serialized_order, broadcast=True, namespace='/ws')


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

    # if config_name == 'development':
    #     # CORS enabled only for development at the moment
    #     CORS(app)

    return app
