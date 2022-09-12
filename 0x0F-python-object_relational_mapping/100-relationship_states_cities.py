#!/usr/bin/python3
"""
Add the State object 'California' with the city 'San Francisco'
to the database hbtn_0e_100_usa using the SQLAlchemy module
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    Cali = State(name='California')
    SanFran = City(name='San Francisco')
    Cali.cities = [SanFran]
    session.add(Cali)
    session.commit()
