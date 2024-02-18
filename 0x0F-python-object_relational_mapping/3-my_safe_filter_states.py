#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
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
    match = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
