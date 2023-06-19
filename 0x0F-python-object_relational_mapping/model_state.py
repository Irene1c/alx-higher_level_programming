#!/usr/bin/python3
"""contains the class definition of a State and an
    instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
import MySQLdb


db = MySQLdb.connect(host="localhost", port=3306,
                     user=argv[1], passwd=argv[2], db=argv[3])


Base = declarative_base()


class State(Base):
    """State class that corresponds to the states table"""

    __tablename__ = 'states'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/:3306{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
