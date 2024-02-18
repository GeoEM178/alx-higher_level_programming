#!/usr/bin/python3
""" prints the State object with the name pswdsed as argument from the database
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
    new_state = State(name='Louisiana')
    session.add(new_state)
    new_t_obj = session.query(State).filter_by(name='Louisiana').first()
    print(new_t_obj.id)
    session.commit()
