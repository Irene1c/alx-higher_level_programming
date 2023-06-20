#!/usr/bin/python3
"""contains the class definition of City """
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class that corresponds to the cities table"""

    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
