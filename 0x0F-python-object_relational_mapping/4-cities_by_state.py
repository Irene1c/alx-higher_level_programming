#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv, exit


if __name__ == "__main__":

    if len(argv) < 4:
        exit()

    user = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=database)
    cur = db.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM cities INNER\
    JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC"
    cur.execute(query)
    row_cities = cur.fetchall()
    for i in row_cities:
        print(i)

    cur.close()
    db.close()
