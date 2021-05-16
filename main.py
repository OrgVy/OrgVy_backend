from flask import Flask
from flask import redirect
from Audiovisual.AudioVisual import AudioVisual
from Audiovisual.Category import Category
from Audiovisual.Type import Type
import logger

app = Flask(__name__)
app.register_blueprint(AudioVisual)
app.register_blueprint(Category)
app.register_blueprint(Type)


@app.errorhandler(404)
def page_not_found(e):
    return {"route": "/404"}, 404


if __name__ == "__main__":
    app.run()
