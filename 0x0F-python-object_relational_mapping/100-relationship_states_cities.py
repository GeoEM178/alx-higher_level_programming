#!/arg_most/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    arg_most=sys.argv[1]
    arg_sr=sys.argv[2]
    db=sys.argv[3]
    host="localhost:3306"
    the_new_eng = create_engine(f'mysql+mysqldb://{arg_most}:{arg_sr}@{host}/{db}',
                           pool_pre_ping=True)
    Base.metadata.create_all(the_new_eng)

    Session = sessionmaker(bind=the_new_eng)
    new_session = Session()

    newState = State(name='California')
    newCity = City(name='San Francisco')
    newState.cities.append(newCity)

    new_session.add(newState)
    new_session.add(newCity)
    new_session.commit()
