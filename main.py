# export FLASK_APP=main.py
from flask import Flask
from flask import redirect
from AudioVisual import AudioVisual

app = Flask(__name__)

app.register_blueprint(AudioVisual)


@app.errorhandler(404)
def page_not_found(e):
    return redirect("/404", code=302)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/404")
def _404():
    return "404 not found", 404


if __name__ == "__main__":
    app.run()
