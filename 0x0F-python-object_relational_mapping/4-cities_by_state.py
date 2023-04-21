#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa"""
from sys import argv
import MySQLdb


def sqlConection():
    """
    Here, Conect and query The database
    """
    try:
        db_connection = MySQLdb.connect(host="localhost", port=3306,
                                        user=argv[1], password=argv[2],
                                        db=argv[3], charset="utf8")
    except Exception:
        print("Can't connect to database")
        return 0
    cur = db_con.cursor()
    sql = "SELECT c.id,c.name, s.name FROM cities AS c JOIN states AS s "
    string = "WHERE c.state_id=s.id ORDER BY id ASC"
    sqlconsc = sql + string
    cur.execute(sqlconsc)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db_con.close()


sqlConection()
