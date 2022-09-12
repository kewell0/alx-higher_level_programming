#!/usr/bin/python3
"""
Change the name of a State object from the database hbtn_0e_6_usa
using the SQLAlchemy module
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

    my_state = session.query(State).get(2)
    my_state.name = "New Mexico"
    session.add(my_state)
    session.commit()
