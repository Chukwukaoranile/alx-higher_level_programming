#!/usr/bin/python3
import MySQLdb
from sys import argv


def mysqlconnnect():
    """
    Connect and query data base from code base
    """
    try:
        db_con = MySQLdb.connect(host="localhost", port=3306,
                                        user=argv[1], passwd=argv[2],
                                        db=argv[3], charset="utf8")
    except Exception:
        print("can't connect to database")
        return 0
    cur = db_con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db_con.close()


mysqlconnnect()
