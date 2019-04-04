from webserver import socketio
from flask_socketio import emit


@socketio.on('message', namespace='/ws')
def socketlistenmessage(message):
    print('RECEIVED MESSAGE {}'.format(message))


@socketio.on('connect', namespace='/ws')
def test_connect():
    print('CONNECTED!!!!!!!')
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/ws')
def test_disconnect():
    print('Client disconnected!')
