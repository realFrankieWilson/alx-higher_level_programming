#!/usr/bin/python3
'''
Takes the name of a state as an argument and list all cities of that state.
'''
import MySQLdb as msd
from sys import argv


def mysqlcon():
    conn = None
    conn = msd.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
            )

    curs = conn.cursor()
    curs.execute(
            "SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s", (argv[4], )
            )

    print(', '.join(city[0] for city in curs.fetchall()))

    curs.close()
    conn.close()


if __name__ == '__main__':
    mysqlcon()
