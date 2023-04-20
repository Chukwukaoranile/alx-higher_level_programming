#!/usr/bin/python3
import MySQLdb
from sys import argv


def mysqlconnnect():
    """
    Connwct and querry the database through the code base
    """
    try:
        db_connection = MySQLdb.connect(host="localhost", port=3306,
                                        user=argv[1], passwd=argv[2],
                                        db=argv[3], charset="utf8")
    except Exception:
        print("can't connect to database")
        return 0
    me = db_connection.cursor()
    me.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = me.fetchall()
    for row in query_rows:
        print(row)
    me.close()
    db_connection.close()


mysqlconnnect()
