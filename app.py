# -*- coding: utf-8 -*-

from flask import Flask, send_from_directory, Response, request, jsonify, render_template
import json
import os
import sys
import getopt
import pymysql
import numpy as np

# app = Flask(__name__, static_url_path='', static_folder='')
# app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

app = Flask(__name__)

#import logging
#logging.basicConfig(level=logging.DEBUG)
#logging.getLogger('matplotlib.font_manager').disabled = True
# cors = CORS(app, allow_headers='Content-Type')

#code shared by Jamil (untested)
def store_user_database(name, email, phone, interest):

    connection = pymysql.connect(host='localhost', user='root', password='admin', db='user_info')

    with connection:
        with connection.cursor() as cursor:
            # Create new records
            sql = "INSERT INTO "
            cursor.execute(sql, (str(i+1), temp_movie_genre_id[i], genre_id[i]))

        # connection is not autocommit by default. So you must commit to save our changes.
        connection.commit()
    return True #False if an issue occured however commit() does not seem to return anything

def send_results_to_user(user_interest):
    connection = pymysql.connect(host='localhost', user='root', password='admin', db='business_owner_info')

    with connection:
        with connection.cursor() as cursor:
            sql = """
            SELECT business_name, business_type, email 
            FROM busines_owner_info bo 
            WHERE bo.business_type = {user_interest}""".format(user_interest = user_interest)
        iterator = cursor.execute(sql)
    return list(iterator)

@app.route("/api/addUser/<string:userInfo>")
def addUser(userInfo):
    """Get user info as name=email=interests=phone with intersts a comma seperated list"""
    print(userInfo)
    name, email, interests, phone = userInfo.split('=')
    interests = interests.split(',')
    if store_user_database(name, email, phone, interest):
        return "200"
    return "500"

@app.route("/api/getInterests<string:intersts>")
def getInterests(interests):
    interests = interests.split(',')
    business = []
    for interest in interests:
        business += send_results_to_user(interests)
    return json.dumps({"business": list(business)})

@app.route("/")
def index():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "p:d", ["port"])

    port = 5000

    for opt, arg in opts:
        if opt in ("-p", "--port"):
            port = int(arg)

    app.run(host='0.0.0.0', port=port)
