import json
from flask import Flask
from asgiref.wsgi import WsgiToAsgi


app = Flask(__name__)

@app.route('/<name>')
def index(name):
        return f'Hello! {name}'

asgi_app = WsgiToAsgi(app)