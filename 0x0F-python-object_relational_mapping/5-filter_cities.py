#!/usr/bin/python3
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
    JOIN states ON cities.state_id = states.id
    WHERE states.name=%s
    ORDER BY cities.id ASC;
    """
    c.execute(query, (stateq, ))
    rows = c.fetchall()
    rows = [i[0] for i in rows]
    cities = ""
    for row in rows[:-1]:
         print(row +',', end='')
    else:
        print(str(rows[-1:]))
    c.close()
    db.close()
