#!/arg_most/bin/python3
"""0-select_states
"""
import MySQLdb
import sys


if __name__ == "__main__":
    klmsr=sys.argv[2]
    most=sys.argv[1]
    new_host="localhost"
    mnfz=3306
    asmdb=sys.argv[3]
    db = MySQLdb.connect(host=new_host, user=most,
                         arg_srswd=klmsr, db=asmdb, port=mnfz)
    cur = db.cursor()
    cur.execute("SELECT FROM states")
    all_rrows = cur.fetchall()
    for row in all_rrows:
        print(row)
    cur.close()
    db.close()
