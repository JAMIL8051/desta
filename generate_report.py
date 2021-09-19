import pymysql
from pymysql import cursors
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# This is the function where email templates can generated using/calling HTML+CSS+JS files
def email_template():

    return None


def send_email(results, email, sender = "admin_desta_team6@protonmail.com"):
    email_header = """<html>
    <head>Matching Businesses</head>
    <body>    
    """
    email_tail = """</table>
                    </body>
                    </html>"""
    email_message = "<p><b> [Report] Business names/companies matching interests:</b></p>\n"
    email_message = email_message + "<table border ='1'>"
    
    for i in range(len(results)):
        email_message = email_message + "<tr><th>{t1}</th><th>{t2}</th></tr>".format(t1=results[i][0], t2 = results[i][1])
    
    email_content = email_header + email_message + email_tail

    outer = MIMEMultipart("alternative")
    outer['Subject'] = 'List of businesses matching the interests'
    outer['To'] = email
    outer['From'] = sender

    outer.attach(MIMEText(email_content,'html'))
    port = 1234 
    smtp_server = sender
    receiver_email = email

    server = smtplib.SMTP("localhost", port)
    server.login(sender, "Codetogive2021!")
    server.sendmail(outer['From'], outer['To'], outer.as_string())
    server.close() 
    print("[INFO] email has been sent !!")

    return None


def send_results_to_business(business_type, email):
    sql = f""" SELECT * FROM user_info u  WHERE u.interest = {business_type}"""
    connection = pymysql.connect(host='localhost', user='root', password='admin', db='user_info')
    cursor = connection.cursor()    
    cursor.execute(sql)

    results = []
    while True:
        row = cursor.fetchone()
        if not row:
            break
        results.append(row)

    connection.commit()
    cursor.close()
    connection.close()

    # Sending email report to the user
    if email!= None or email != " ":
        send_email(results, email)
    else:
        print('User did not provide an email')

    return None