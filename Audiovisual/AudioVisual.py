from flask import Blueprint

AudioVisual = Blueprint('AudioVisual', __name__, url_prefix="/audio-visual")


@AudioVisual.route("/")
def main():
    return "main"


@AudioVisual.route("/hello")
def accountList():
    return "hello audiovisual"
