#!/usr/bin/python3
""" Lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
from sys import argv


def mysqlcon():
    conn = None
    conn = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
            )

    cur = conn.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id \
            ORDER BY cities.id ASC")

    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    conn.close()


if __name__ == '__main__':
    mysqlcon()
