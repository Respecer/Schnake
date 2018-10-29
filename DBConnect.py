import mysql.connector
from mysql.connector import Error

class DBConnect:
    def __init__(self, hostname, dbname, username, pw):
        try:
            self.connection = mysql.connector.connect(host=hostname,
                                           database=dbname,
                                           user=username,
                                           password=pw)
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(e)
        finally:
            self.connection.close()
