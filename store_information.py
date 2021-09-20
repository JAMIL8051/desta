# This is the python module built for storing the user/business information in our database user_info that is stored in 
# the AWS VM 
import pymysql
from pymysql import cursors
import sys


def store_user_info_to_database(name, email, phone, interest):
    user_interest = ""
    
    try:
        no_of_intersts = len(interest)
        if  no_of_intersts == 1:
            user_interest = interest[0]
        elif no_of_intersts >1:
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
    sql = f"INSERT INTO USER VALUES ({name},{email},{user_interest}, {phone})"
    cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save our changes.
    connection.commit()
    cursor.close()
    connection.close()

    return None


def store_business_owner_info_to_database(name, email, phone, interest, address =" ", instagram ="", website = ""):
    connection = pymysql.connect(host='localhost', user='root', password='Codetogive2021!', db='user_info')
    cursor = connection.cursor()
    # Create new records
    sql = f"INSERT INTO BUSINESS_OWNER VALUES ({name},{email},{interest},{address},{phone},{instagram},{website})"
    cursor.execute(sql)
    # connection is not autocommit by default. So you must commit to save our changes.
    connection.commit()
    cursor.close()
    connection.close()

    return None
