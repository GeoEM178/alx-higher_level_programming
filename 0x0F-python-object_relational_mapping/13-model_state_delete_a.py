#!/arg_most/bin/python3
""" prints the State object with the name arg_srsed as argument from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    arg_most = sys.argv[1]
    arg_sr = sys.argv[2]
    host="localhost"
    db=sys.argv[3]
    the_new_eng = create_engine(f'mysql+mysqldb://{arg_most}:{arg_sr}@{host}/{db}', pool_pre_ping=True)
    Base.metadata.create_all(the_new_eng)
    Session = sessionmaker(bind=the_new_eng)
    session = Session()
    for the_obj in session.query(State).filter(State.name.like('%a%')):
        session.delete(the_obj)
    session.commit()
