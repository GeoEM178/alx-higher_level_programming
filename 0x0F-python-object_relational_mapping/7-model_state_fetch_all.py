#!/usr/bin/python3
"""Start link class to table in database
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
    new_session = Session()
    for t_obj in new_session.query(State).order_by(State.id):
        print(t_obj.id, t_obj.name, sep=": ")
