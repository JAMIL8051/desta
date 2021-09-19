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

def store_user_info_to_database(name, email, phone, interest):
    user_interest = ""
    
    try:
        no_of_intersts = len(interest)
        if  no_of_intersts == 1:
            user_interest = interest[0]
        elif no_of_intersts > 1:
            for val in interest:
                user_interest = user_interest + str(val) + ","
        elif no_of_intersts == 0:
            user_interest = user_interest
        
        user_interest = user_interest[:-1] # We are avoiding the last comma

    except Exception as e:
        print(e)
        sys.exit(1)

    connection = pymysql.connect(host='localhost', user='root', password='Codetogive2021!', db='user_info')
    cursor = connection.cursor() 
    # Create new records
    sql = f"INSERT INTO USER VALUES ({name},{email},{user_interest},{phone})"
    cursor.execute(sql)
    # connection is not autocommit by default. So you must commit to save our changes.
    connection.commit()
    cursor.close()
    connection.close()

    return None


def send_results_to_user(user_interest, email):
    sql = f"SELECT name, email FROM BUSINESS_OWNER bo WHERE bo.business_type = {user_interest}"

    connection = pymysql.connect(host='localhost', user='root', password='Codetogive2021!', db='user_info')
    cursor = connection.cursor() 
    iterator = cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()
    
    return list(iterator)
@app.route("/api/addUser/<string:userInfo>")
def addUser(userInfo):
    """Get user info as name=email=interests=phone with intersts a comma seperated list"""
    print(userInfo)
    name, email, interests, phone = userInfo.split('=')
    interests = interests.split(',')
    if store_user_database(name, email, phone, interests):
        return "200"
    return "500"
@app.route("/api/addUser/<string:businessInfo>")
def addUser(businessInfo):
    """Get business owner info as name=email=interests=address=phone with intersts a comma seperated list"""
    print(businessInfo)
    name, email, interests, address, phone = businessInfo.split('=')
    interests = interests.split(',')
    if store_information.store_business_owner_info_to_database(name, email, address, phone, interests):
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
