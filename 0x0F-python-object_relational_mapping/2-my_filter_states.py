#!/usr/bin/python3
"""Connect DataBase Takes an Argument and find a match"""


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
            "SELECT * FROM states WHERE name LIKE BINARY '{}"
            "ORDER BY states.id ASC".format(sys.argv[4])
            )

    selected_row = cur.fetchall()

    for state in selected_row:
        print(state)

    cur.close()


if __name__ == '__main__':
    mysqlcon()
