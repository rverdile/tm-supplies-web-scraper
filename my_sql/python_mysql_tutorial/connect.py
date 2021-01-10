import mysql.connector
from mysql.connector import Error

def connect():

    conn = None

    try:
        conn = mysql.connector.connect( host='localhost',
                                        port=3306, # replace with port (might be the same)
                                        user='', # replace with name of user
                                        password='') # replace with password

        if conn.is_connected():
            print("Connected to MySQL database")

    except Error as e:
        print(e)


    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':

    connect()




                                                