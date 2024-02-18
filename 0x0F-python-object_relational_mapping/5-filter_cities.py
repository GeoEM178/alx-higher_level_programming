#!/usr/bin/python3
""" a script that takes in the name of a state as an argument 
    and lists all cities of that state, using the database hbtn_0e_4_usa
"""
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
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    all_rows = cur.fetchall()
    tmp = list(row[0] for row in all_rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
