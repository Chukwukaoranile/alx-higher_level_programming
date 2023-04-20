#!/usr/bin/python3
from sys import argv
import MySQLdb


def connectDB():
    """
    Connecting the database and query it through the code base
    """
    try:
        db_connection = MySQLdb.connect(host="localhost", port=3306,
                                        user=argv[1], password=argv[2],
                                        db=argv[3], charset="utf8")
    except Exception:
        print("Can't connect to database")
        return 0
    mem = db_connection.cursor()
    sql = "SELECT id, name FROM states ORDER BY id ASC;"
    mem.execute(sql)
    query_rows = mem.fetchall()
    for row in query_rows:
        if 'N' == row[1][0]:
            print(row)
    mem.close()
    db_connection.close()


connectDB()
