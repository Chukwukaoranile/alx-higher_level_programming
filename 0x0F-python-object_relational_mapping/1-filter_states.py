#!/usr/bin/python3
from sys import argv
import MySQLdb


def connectDB():
    """
    Connecting the database and query it through the code base
    """
    if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    me = db.cursor()
    myQuery = " ".join([
        "SELECT * FROM states",
        "WHERE name LIKE BINARY 'N%'",
        "ORDER BY id ASC"])
    me.execute(myQuery)
    res = me.fetchall()
    for rows in res:
        print(rows)
    me.close()
    db.close()
