#!/usr/bin/python3
"""
Define a class State and an instance Base using the sqlalchemy ORM
"""

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """Definition of class State
    Parameters:
        id (int): unique identifier for each state
        name (string): name of the state
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
