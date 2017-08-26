# Microservice to authenticate a user
# Reference: http://flask.pocoo.org/

from flask import Flask
import mysql.connector
import requests

app = Flask(__name__)

cnx = mysql.connector.connect(user='authentication_user',
                              password='password',
                              host='localhost',
                              database='authentication-db')
cursor = cnx.cursor()

@app.route('/id/<string:id>/password/<string:password>/resource_id/<string:resource>', methods=['GET'])
def authenticate_user(id, password, resource):
    """This function performs user authentication by checking the DB table 'authentications'
    and forwards the request to authorization service
    :param id: User ID
    :param password: User password
    :param resource: The requested resource
    :return: The http response
    """
    global cursor
    query = "SELECT COUNT(*) AS cnt FROM `authentications` WHERE user_id=%s AND user_pwd=%s;"
    cursor.execute(query, [id, password])
    count = cursor.fetchone()[0]
    if count >= 1:
        host = "localhost"
        port = 3000
        url = 'http://%s:%d/id/%s/%s/' % (host, port, id, resource)
        print "url ->", url
        r = requests.get(url)
        return r.text, r.status_code
    else:
        bad_credentials = 401
        return "You are not authentic user", bad_credentials

if __name__ == '__main__':
    app.run(port=5000)