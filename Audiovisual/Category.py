from flask import request

from . import Category
import Database.connectionDB as connectionDB


@Category.route("", methods=['GET'])
def get_categories():
    if request.method == 'GET':
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
    else:
        return "405 Method Not Allowed", 405
