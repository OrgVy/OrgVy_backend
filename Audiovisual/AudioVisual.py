from flask import Blueprint
import Database.connectionDB as connectionDB

AudioVisual = Blueprint('AudioVisual', __name__, url_prefix="/audio-visual")


@AudioVisual.route("/")
def get_categories():
    try:
        connection = connectionDB.open_connection()
        connection_cursor = connection.cursor()
        connection_cursor.execute("SELECT * FROM OrgVy.category;")
        result = connection_cursor.fetchall()
        aux = []
        for category in result:
            aux.append(category[1].__str__())
        connection_cursor.close()
        connection.close()
        return {"categories": aux}, 200
    except:
        return 500



@AudioVisual.route("/hello")
def accountList():
    return "hello audiovisual"
