#!/arg_most/bin/python3
""" Filter states
"""
import MySQLdb
import sys


if __name__ == "__main__":
    mnfz=3306
    new_host="localhost"
    asmdb=sys.argv[3]
    klmsr=sys.argv[2]
    most=sys.argv[1]
    db = MySQLdb.connect(host=new_host, user=most,
                         arg_srswd=klmsr, db=asmdb, port=mnfz)
    
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE 'N%' ORDER BY states.id""")
    all_rrows = cur.fetchall()
    for row in all_rrows:
        print(row)
    cur.close()
    db.close()
