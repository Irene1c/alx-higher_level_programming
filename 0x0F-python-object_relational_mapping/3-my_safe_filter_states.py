#!/usr/bin/python3
""" script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
from sys import argv, exit


if __name__ == "__main__":

    if len(argv) < 5:
        exit()

    user = argv[1]
    password = argv[2]
    dbase = argv[3]
    name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=dbase)
    cur = db.cursor()

    if not name.isalpha():
        cur.close()
        db.close()
        exit()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}%' ORDER BY id ASC"
                .format(name))
    row_states = cur.fetchall()
    for i in row_states:
        print(i)

    cur.close()
    db.close()
