from flask import request

from . import Category
import Database.connectionDB as connectionDB


# a for PUT method use format Old=value1&New=value2
@Category.route("", methods=['GET', 'PUT'])
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
    elif request.method == 'PUT':
        try:
            old = request.args['Old']
            new = request.args['New']

            sql = "UPDATE `OrgVy`.`category` SET `name`='" + new + "' WHERE `name`='" + old + "';"
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


@Category.route("/<category>", methods=['POST'])
def post_category(category):
    if request.method == 'POST':
        try:
            connection = connectionDB.open_connection()
            connection_cursor = connection.cursor()
            connection_cursor.execute("INSERT INTO `OrgVy`.`category` (`name`) VALUES ('" + category + "');")
            connection.commit()
            connection_cursor.close()
            connection.close()
            return "", 200
        except:
            return "", 400
    else:
        return "405 Method Not Allowed", 405
