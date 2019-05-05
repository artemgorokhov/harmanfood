import webserver

app = webserver.create_app('production')

if __name__ == '__main__':
    webserver.socketio.run(app,
                           host='0.0.0.0',
                           port=5000,
                           debug=False)
