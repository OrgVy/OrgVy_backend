from . import Type
from flask import request
import Database.connectionDB as connectionDB


# a for PUT method use format Old=value1&New=value2
@Type.route("", methods=['GET', 'PUT'])
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
    elif request.method == 'PUT':
        try:
            old = request.args['Old']
            new = request.args['New']

            sql = "UPDATE `OrgVy`.`type` SET `name`='" + new + "' WHERE `name`='" + old + "';"
            connection = connectionDB.open_connection()
            connection_cursor = connection.cursor()
            connection_cursor.execute(sql)
            connection.commit()
            connection_cursor.close()
            connection.close()

            return "", 200
        except:
            return 500
    else:
        return "405 Method Not Allowed", 405


@Type.route("/<type>", methods=['POST'])
def post_category(type):
    if request.method == 'POST':
        try:
            connection = connectionDB.open_connection()
            connection_cursor = connection.cursor()
            connection_cursor.execute("INSERT INTO `OrgVy`.`type` (`name`) VALUES ('" + type + "');")
            connection.commit()
            connection_cursor.close()
            connection.close()
            return "", 200
        except:
            return "", 400
    else:
        return "405 Method Not Allowed", 405
