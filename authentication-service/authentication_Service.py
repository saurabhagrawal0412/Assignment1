# Microservice to authenticate a user
# Reference: https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html

from flask import Flask
from flask_restful import Resource, Api
import mysql.connector

app = Flask(__name__)
api = Api(app)

cnx = mysql.connector.connect(user='authentication_user',
                              password='password',
                              host='localhost',
                              database='authentication-db')
cursor = cnx.cursor()

class Authenticator(Resource):
    def get(self, id, password):
        global cursor
        query = "SELECT COUNT(*) AS cnt FROM `authentications` WHERE user_id=%s AND user_pwd=%s;"
        cursor.execute(query, [id, password])
        count = cursor.fetchone()[0]
        if count >= 1:
            return "You are authentic user"
        else:
            return "You are not authentic user"

api.add_resource(Authenticator, '/id/<string:id>/password/<string:password>')

if __name__ == '__main__':
    app.run()
