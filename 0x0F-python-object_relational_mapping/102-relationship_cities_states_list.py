#!/arg_most/bin/python3
""" prints the State object with the name arg_srsed as argument from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    arg_most = sys.argv[1]
    arg_sr = sys.argv[2]
    host="localhost"
    db=sys.argv[3]
    the_new_eng = create_engine(f'mysql+mysqldb://{arg_most}:{arg_sr}@{host}/{db}', pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for the_obj in session.query(State).order_by(State.id):
        for city_ins in the_obj.cities:
            print(city_ins.id, city_ins.name, sep=": ", end="")
            print(" -> " + the_obj.name)
