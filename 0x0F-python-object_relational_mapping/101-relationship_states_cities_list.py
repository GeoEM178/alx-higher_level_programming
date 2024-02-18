#!/usr/bin/python3
""" prints the State object with the name pswdsed as argument from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    usr = sys.argv[1]
    pswd = sys.argv[2]
    host="localhost"
    db=sys.argv[3]
    the_created_eng = create_engine(f'mysql+mysqldb://{usr}:{pswd}@{host}/{db}', pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for t_obj in session.query(State).order_by(State.id):
        print(t_obj.id, t_obj.name, sep=": ")
        for city_ins in t_obj.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
