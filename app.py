import pafy
from flask import Flask,render_template
from asgiref.wsgi import WsgiToAsgi


app = Flask(__name__)


@app.route("/")
def index():
    url = "https://www.youtube.com/watch?v=6U1wyOyuzj4"
    #video = pafy.new(url)video.getbestaudio().url

    return render_template("index.html", url = url)
    #return "video.getbestaudio().url"


asgi_app = WsgiToAsgi(app)
