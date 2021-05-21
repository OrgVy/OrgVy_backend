from flask import request

from . import User
import Database.connectionDB as connectionDB


@User.route("", methods=['GET', 'POST', 'PUT'])
def user():
    try:
        data = request.get_json()
        email = data["Email"]
        password = data["Password"]
    except:
        return {"400": "Bad request"}, 400
    if request.method == 'POST':
        try:
            try:
                name = data["Name"]
            except:
                return {"400": "Bad request"}, 400

            connection = connectionDB.open_connection()
            connection_cursor = connection.cursor()
            connection_cursor.execute("INSERT INTO `users` (`name`,`email`,`password`) "
                                      "VALUES ('" + name + "', '" + email + "', '" + password + "');")
            connection.commit()
            connection_cursor.close()
            connection.close()
            return "", 200
        except:
            return 500
    elif request.method == 'GET':
        try:
            connection = connectionDB.open_connection()
            connection_cursor = connection.cursor()
            connection_cursor.execute(
                "SELECT * FROM users WHERE `email`='" + email + "' and `password`='" + password + "';")
            result = connection_cursor.fetchall()
            connection_cursor.close()
            connection.close()
            if len(result) == 1:
                user = {
                    "name": result[0][0],
                    "email": result[0][1]
                }
                return user, 200
            elif len(result) == 0:
                return {}, 200
            else:
                return "ESTO NUNCA DEBERIA PASAR", 500
        except:
            return 500
    elif request.method == 'PUT':
        try:
            try:
                new_name = data["Name"]
                new_email = data["New_email"]
                new_password = data["New_password"]
            except:
                return {"400": "Bad request"}, 400

            sql = "UPDATE `users` SET `name`='" + new_name + "', `email`='" + new_email + "', `password`='" + new_password + "' WHERE `email`='" + email + "';"
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

