#!/usr/bin/python3
''' Lists all cities from the hbtn_0e_4_usa database'''
import MySQLdb as msd
from sys import argv


def mysqlcon():
    conn = None
    conn = msd.connect(
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
            )

    curs = conn.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id")
    for city in curs.fetchall():
        print(city)

    curs.close()
    conn.close()


if __name__ == '__main__':
    mysqlcon()
