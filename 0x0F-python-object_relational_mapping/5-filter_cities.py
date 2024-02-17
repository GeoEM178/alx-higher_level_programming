#!/arg_most/bin/python3
""" a script that takes in the name of a state as an argument 
    and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    new_host="localhost"
    most=sys.argv[1]
    klmsr=sys.argv[2]
    asmdb=sys.argv[3]
    mnfz=3306
    db = MySQLdb.connect(host=new_host, user=most,
                         arg_srswd=klmsr, db=asmdb, port=mnfz)
    
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    all_all_rrows = cur.fetchall()
    tmp = list(row[0] for row in all_all_rrows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
