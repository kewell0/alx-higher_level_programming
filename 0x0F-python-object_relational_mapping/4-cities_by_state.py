#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         password=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    SQL = "SELECT cities.id, cities.name, states.name\
           FROM cities\
           INNER JOIN states\
           ON cities.state_id = states.id\
           ORDER BY cities.id ASC"
    cursor.execute(SQL)
    cities = cursor.fetchall()
    if cities is not None:
        for row in cities:
            print("({}, '{}', '{}')".format(row[0], row[1], row[2]))
        cursor.close()
        db.close()
