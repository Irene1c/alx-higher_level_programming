#!/usr/bin/python3
""" script that changes the name of a State
    object from the database
"""
from model_state import Base, State
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

    state = session.query(State).get(2)
    state.name = "New Mexico"
    session.add(state)
    session.commit()
