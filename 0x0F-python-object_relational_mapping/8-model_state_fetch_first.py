#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    usr = sys.argv[1]
    pswd = sys.argv[2]
    host="localhost"
    db=sys.argv[3]
    the_created_eng = create_engine(f'mysql+mysqldb://{usr}:{pswd}@{host}/{db}', pool_pre_ping=True)
    Base.metadata.create_all(the_created_eng)
    Session = sessionmaker(bind=the_created_eng)
    session = Session()
    t_obj = session.query(State).first()
    if t_obj is None:
        print("Nothing")
    else:
        print(t_obj.id, t_obj.name, sep=": ")
