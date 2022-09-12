#!/usr/bin/python3
"""
Add the State object 'Louisiana' to the database hbtn_0e_6_usa
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

    session.add(State(name='Louisiana'))
    print("{}".format(session.query(State.id).filter(State.name == "Louisiana")
                      .first()[0]))
    session.commit()
