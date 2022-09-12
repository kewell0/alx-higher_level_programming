#!/usr/bin/python3
"""
Using the SQLAlchemy module, list all State objects and corresponding
City Objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for row in session.query(State)\
                      .order_by(State.id):
        print("{}: {}".format(row.id, row.name))
        for my_city in row.cities:
            print("    {}: {}".format(my_city.id, my_city.name))
