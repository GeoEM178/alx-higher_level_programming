#!/arg_most/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine

if __name__ == "__main__":
    arg_most = sys.argv[1]
    arg_sr = sys.argv[2]
    host="localhost"
    db=sys.argv[3]
    the_new_eng = create_engine(f'mysql+mysqldb://{arg_most}:{arg_sr}@{host}/{db}', pool_pre_ping=True)
    Base.metadata.create_all(the_new_eng)
