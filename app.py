import os
import pafy
from flask import Flask
from asgiref.wsgi import WsgiToAsgi


project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, "app/templates")
app = Flask(__name__, template_folder=template_path)


@app.route("/")
def index():
    url = "https://www.youtube.com/watch?v=6U1wyOyuzj4"
    video = pafy.new(url)

    return video.getbestaudio().url


asgi_app = WsgiToAsgi(app)
