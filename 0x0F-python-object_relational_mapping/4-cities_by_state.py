#!/usr/bin/python3
""" Get data from database """
import MySQLdb
import sys


if __name__ == "__main__":
    dbHost="localhost"
    dbUser=sys.argv[1]
    dbpswdswd=sys.argv[2]
    dbName=sys.argv[3]
    t_port=3306
    db = MySQLdb.connect(host=dbHost, user=dbUser,
                         pswdswd=dbpswdswd, db=dbName, port=t_port)

    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    all_rows = cur.fetchall()
    for row in all_rows:
        print(row)
    cur.close()
    db.close()
