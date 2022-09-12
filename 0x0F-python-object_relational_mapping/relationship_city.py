#!/usr/bin/python3
"""
Define a class State and an instance Base using the sqlalchemy ORM
"""

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer
from relationship_state import Base


class City(Base):
    """Definition of class City
    Parameters:
        id (int): unique identifier for each city
        name (string): name of the city
        state_id (int): ID of state that city is in
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
