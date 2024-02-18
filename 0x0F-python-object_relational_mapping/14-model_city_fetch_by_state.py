#!/usr/bin/python3
""" prints the State object with the name pswdsed as argument from the database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    usr = sys.argv[1]
    pswd = sys.argv[2]
    host="localhost"
    db=sys.argv[3]
    the_created_eng = create_engine(f'mysql+mysqldb://{usr}:{pswd}@{host}/{db}', pool_pre_ping=True)
    Base.metadata.create_all(the_created_eng)
    Session = sessionmaker(bind=the_created_eng)
    new_session = Session()
    for t_obj in (new_session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(t_obj[0] + ": (" + str(t_obj[1]) + ") " + t_obj[2])
