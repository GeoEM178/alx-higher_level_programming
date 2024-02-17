#!/arg_most/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa """
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
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    all_all_rrows = cur.fetchall()
    for row in all_all_rrows:
        print(row)
    cur.close()
    db.close()
