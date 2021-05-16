from . import Type
from flask import request
import Database.connectionDB as connectionDB


@Type.route("", methods=['GET'])
def get_types():
    if request.method == 'GET':
        try:
            connection = connectionDB.open_connection()
            connection_cursor = connection.cursor()
            connection_cursor.execute("SELECT * FROM OrgVy.type;")
            result = connection_cursor.fetchall()
            aux = []
            for type in result:
                aux.append(type[1].__str__())
            connection_cursor.close()
            connection.close()
            return {"types": aux}, 200
        except:
            return 500
    else:
        return "405 Method Not Allowed", 405
