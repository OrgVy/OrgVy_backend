from flask import Blueprint

Login = Blueprint('Login', __name__, url_prefix="/user/login")
User = Blueprint('User', __name__, url_prefix="/user")
