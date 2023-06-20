#!/usr/bin/python3
"""contains the class definition of a State and a
    relationship with City
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class State(Base):
    """State class that corresponds to the states table"""

    __tablename__ = 'states'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City', backref=backref('state', cascade='all, delete'))
