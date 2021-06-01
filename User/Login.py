from flask import request

from . import Login
import Database.connectionDB as connectionDB


@Login.route("", methods=['GET'])
def get_login():
    try:
        email = request.args.get('Email')
        password = request.args.get('Password')
    except:
        return {"400": "Bad request"}, 400
    if request.method == 'GET':
        try:
            connection = connectionDB.open_connection()
            connection_cursor = connection.cursor()
            connection_cursor.execute(
                "SELECT * FROM users WHERE `email`='" + email + "' and `password`='" + password + "';")
            result = connection_cursor.fetchall()
            connection_cursor.close()
            connection.close()

            if len(result) > 1:
                return 500
            elif len(result) == 0:
                return {"isLogin": 0}, 200
            else:
                return {"isLogin": 1}, 200
        except:
            return 500
    else:
        return "405 Method Not Allowed", 405
