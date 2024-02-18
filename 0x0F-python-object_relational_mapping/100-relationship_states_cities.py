#!/usr/bin/python3
"""
Insert into database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    usr=sys.argv[1]
    pswd=sys.argv[2]
    db=sys.argv[3]
    host="localhost:3306"
    the_created_eng = create_engine(f'mysql+mysqldb://{usr}:{pswd}@{host}/{db}',
                           pool_pre_ping=True)
    Base.metadata.create_all(the_created_eng)

    Session = sessionmaker(bind=the_created_eng)
    new_session = Session()

    t_astate = State(name='California')
    t_city = City(name='San Francisco')
    t_astate.cities.append(t_city)

    new_session.add(t_astate)
    new_session.add(t_city)
    new_session.commit()
