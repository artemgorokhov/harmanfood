from flask import Flask

app = Flask(__name__, 
            static_folder='../dist/static',
            template_folder='../dist')
app.secret_key = b'\xf6X\xb7\x98\xe9P\xd0Pi\xb3m\xce\x07i0X'

import webserver.routes
