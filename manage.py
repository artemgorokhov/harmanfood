from flask_script import Manager, Server as _Server, Option
from webserver import create_app, socketio

manager = Manager(create_app)


class Server(_Server):
    help = description = "Runs Socket.IO web server"

    def get_options(self):
        options = (
            Option('-h', '--host',
                   dest='host',
                   default=self.host),

            Option('-p', '--port',
                   dest='port',
                   type=int,
                   default=self.port),

            Option('-d', '--debug',
                   action='store_true',
                   dest='use_debugger',
                   help='DO NOT use in production',
                   default=self.use_debugger),

            Option('-D', '--no-debug',
                   action='store_false',
                   dest='use_debugger',
                   default=self.use_debugger),

            Option('-r', '--reload',
                   action='store_true',
                   dest='use_reloader',
                   default=self.use_reloader),

            Option('-R', '--no-reload',
                   action='store_false',
                   dest='use_reloader',
                   default=self.use_reloader),
        )
        return options

    def __call__(self, app=None, *args, **kwargs):
        print('Running server:')
        print('\tAddress: {}:{}'.format(self.host, self.port))
        print('\tUse debugger: {}'.format(self.use_debugger))
        print('\tUse reloader: {}'.format(self.use_reloader))
        socketio.run(app,
                     host=self.host,
                     port=self.port,
                     debug=self.use_debugger,
                     use_reloader=self.use_reloader,
                     **self.server_options)


manager.add_command("runserver", Server())


if __name__ == '__main__':
    manager.run()
