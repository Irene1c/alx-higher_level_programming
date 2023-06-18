#!/usr/bin/python3
""" script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv, exit


if __name__ == "__main__":

    if len(argv) < 5:
        exit()

    user = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=database)
    cur = db.cursor()

    if not name.isalpha():
        cur.close()
        db.close()
        exit()

    query = "SELECT cities.name FROM cities INNER JOIN states ON states.id\
            = cities.state_id WHERE states.name LIKE %s ORDER BY cities.id ASC"
    cur.execute(query, (name + '%',))
    row_cities = cur.fetchall()
    cities = list(i[0] for i in row_cities)
    print(', '.join(cities))

    cur.close()
    db.close()
