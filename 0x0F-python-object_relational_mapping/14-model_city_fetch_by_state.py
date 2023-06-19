#!/usr/bin/python3
""" script that prints all City objects from the database hbtn_0e_14_usa"""
from model_state import Base, State
from model_city import City
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

    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(City, State).join(State).order_by(City.id.asc()).all()
    for city, state in q:
        print(f"{state.name}: ({city.id}) {city.name}")
