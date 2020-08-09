#!/usr/bin/python3
""" List all states in MYSQL database"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    c = db.cursor()
    c.execute("SELECT states.id, name FROM states WHERE name "
              "COLLATE latin1_general_cs LIKE 'N%' "
              "ORDER BY states.id ASC;")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
