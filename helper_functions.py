import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pymysql
from pymysql import cursors


def handle_frontend_request():
    return None

def store_user_info_to_database(name, email):
    connection = pymysql.connect(host='localhost', user='root', password='admin', db='user_info')

    with connection:
        with connection.cursor() as cursor:
            # Create new records
            sql = "INSERT INTO "
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save our changes.
        connection.commit()








def send_results_to_user(interest, email, type):
    connection = pymysql.connect(host='localhost', user='root', password='admin', db='business_owner_info')

    with connection:
        with connection.cursor() as cursor:
            sql = """
            SELECT business_name, business_type, email 
            FROM busines_owner_info bo 
            WHERE bo.business_type = {user_interest}""".format(user_interest = interest)
        cursor.execute(sql)

        results = []
        while True:
            row = cursor.fetchone()
            if not row:
                break
            results.append(row)
        
        cursor.close()

        # Sending email report to the user
        if email!= None or email != " ":
            send_email(results, email)
        else:
            print('User did not provide an email')

    return None


        


        
