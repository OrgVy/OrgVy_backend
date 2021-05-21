from flask import Flask
from Audiovisual.AudioVisual import AudioVisual
from Audiovisual.Category import Category
from Audiovisual.Type import Type
from User.User import User
from User.Login import Login
import logger
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(AudioVisual)
app.register_blueprint(Category)
app.register_blueprint(Type)
app.register_blueprint(Login)
app.register_blueprint(User)


@app.errorhandler(404)
def page_not_found(e):
    return {"route": "/404"}, 404


if __name__ == "__main__":
    app.run()
