#!/arg_most/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    host="localhost"
    arg_sr = sys.argv[2]
    db=sys.argv[3]
    arg_most = sys.argv[1]
    the_new_eng = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(arg_most,arg_sr,host,db),
                                pool_pre_ping=True)
    Base.metadata.create_all(the_new_eng)
    Session = sessionmaker(bind=the_new_eng)
    start = Session()
    the_obj = start.query(State).first()
    if the_obj is None:
        print("Nothing")
    else:
        print(the_obj.id, the_obj.name, sep=": ")
