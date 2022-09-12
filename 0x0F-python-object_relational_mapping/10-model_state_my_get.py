#!/usr/bin/python3
"""
Using the SQLAlchemy module, list the State object
from the database hbtn_0e_6_usa with the name passed as an argument
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(State).filter(State.name == sys.argv[4]).one_or_none()
    if row:
        print("{}".format(row.id))
    else:
        print("Not found")
