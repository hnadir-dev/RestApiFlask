import pafy
from flask import Flask
from asgiref.wsgi import WsgiToAsgi


app = Flask(__name__)


@app.route("/")
def index():
    url = "https://www.youtube.com/watch?v=6U1wyOyuzj4"
    video = pafy.new(url)

    return video.getbestaudio().url


asgi_app = WsgiToAsgi(app)
