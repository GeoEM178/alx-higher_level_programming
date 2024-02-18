#!/usr/bin/python3
"""  script that takes in an argument and displays all values 
     in the states table of hbtn_0e_0_usa where name matches the argument. 
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
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
