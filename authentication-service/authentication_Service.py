# Microservice to authenticate a user
# Reference: https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html

from flask import Flask
from flask_restful import Resource, Api
import requests
import mysql.connector

app = Flask(__name__)
api = Api(app)

cnx = mysql.connector.connect(user='authentication_user',
                              password='password',
                              host='localhost',
                              database='authentication-db')
cursor = cnx.cursor()

class Authenticator(Resource):
    def get(self, id, password, resource):
        global cursor
        query = "SELECT COUNT(*) AS cnt FROM `authentications` WHERE user_id=%s AND user_pwd=%s;"
        cursor.execute(query, [id, password])
        count = cursor.fetchone()[0]
        if count >= 1:
            host = "localhost"
            port = 3000
            url = 'http://%s:%d/id/%s/%s/' %(host, port, id, resource)
            print "url ->", url
            r = requests.get(url)
            return r.text, r.status_code
        else:
            bad_credentials = 401
            return "You are not authentic user", bad_credentials

api.add_resource(Authenticator, '/id/<string:id>/password/<string:password>/resource_id/<string:resource>')

if __name__ == '__main__':
    app.run()
