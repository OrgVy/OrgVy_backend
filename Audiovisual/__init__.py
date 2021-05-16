from flask import Blueprint

AudioVisual = Blueprint('AudioVisual', __name__, url_prefix="/audiovisual")
Category = Blueprint('Category', __name__, url_prefix="/audiovisual/category")
Type = Blueprint('Type', __name__, url_prefix="/audiovisual/type")
