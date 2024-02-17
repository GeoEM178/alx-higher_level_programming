#!/arg_most/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
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
    match = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    all_rrows = cur.fetchall()
    for row in all_rrows:
        print(row)
    cur.close()
    db.close()
