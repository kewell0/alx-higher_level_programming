#!/usr/bin/python3
"""
Script that lists states from the database hbtn_0e_0_usa that match a given
argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    SQL = "SELECT id, name\
           FROM states\
           WHERE BINARY name = '{}'\
           ORDER BY id ASC".format(sys.argv[4])
    cursor.execute(SQL)
    states = cursor.fetchall()
    if states is not None:
        [print(state) for state in states]
    cursor.close()
    db.close()
