import json
from flask import Flask
from asgiref.wsgi import WsgiToAsgi


app = Flask(__name__)

@app.route('/')
def index():
        return json.dumps({'name': 'alice','email': 'alice@outlook.com'})

asgi_app = WsgiToAsgi(app)
