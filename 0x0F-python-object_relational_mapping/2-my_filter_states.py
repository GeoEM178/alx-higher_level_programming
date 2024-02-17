#!/arg_most/bin/python3
"""  script that takes in an argument and displays all values 
     in the states table of hbtn_0e_0_usa where name matches the argument. 
"""
import MySQLdb
import sys


if __name__ == "__main__":
    mnfz=3306
    most=sys.argv[1]
    asmdb=sys.argv[3]
    klmsr=sys.argv[2]
    new_host="localhost"
    db = MySQLdb.connect(host=new_host, user=most,
                         arg_srswd=klmsr, db=asmdb, port=mnfz)

    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name LIKE BINARY '{sys.argv[4]}'")
    all_rrows = cur.fetchall()
    for row in all_rrows:
        print(row)
    cur.close()
    db.close()
