#!/usr/bin.py_/python3
""" List all states in MYSQL database"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    stateq = argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    c = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE BINARY states.name LIKE '{}'
    ORDER BY cities.id ASC;
    """.format(stateq)
    c.execute(query)
    rows = c.fetchall()
    for row in rows[:-1]:
        print(str(row[0]) + ', ', end='')
    print(str(rows[-1][0]))
    c.close()
    db.close()
