#!/usr/bin/python3
""" Safe for SQL injection """
import MySQLdb
from sys import argv


def mysqlcon():
    conn = None
    conn = MySQLdb.connect(
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
            )

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (argv[4],))
    states = cur.fetchall()

    for i in states:
        print(i)

    cur.close()
    conn.close()


if __name__ == '__main__':
    mysqlcon()
