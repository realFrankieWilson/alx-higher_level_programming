#!/usr/bin/python3
"""
Connect DataBase and query
And list states with capital N
"""

import MySQLdb
import sys


def mysqlcon():
    conn = None
    conn = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    cur = conn.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE 'N%'"
            "COLLATE Latin1_General_CS;")
            )
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()


if __name__ == '__main__':
    mysqlcon()
