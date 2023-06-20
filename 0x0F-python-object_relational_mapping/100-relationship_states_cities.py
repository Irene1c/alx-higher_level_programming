#!/usr/bin/python3
""" script that creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa
"""
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv, exit


if __name__ == "__main__":
    if len(argv) < 4:
        exit()

    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
            @localhost:3306/{database}', pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='California')
    city = City(name='San Francisco')
    state.cities.append(city)

    session.add(state)
    session.commit()
