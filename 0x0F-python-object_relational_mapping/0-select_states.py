#!/usr/bin/python3
import MySQLdb
from sys import argv


def mysqlconnect():
    """
    Connects to the MySQL database and queries data.
    """
    try:
        db_connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
        )
    except MySQLdb.Error as error:
        print("Can't connect to database: {}".format(error))
        return
    
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db_connection.close()

mysqlconnect()
