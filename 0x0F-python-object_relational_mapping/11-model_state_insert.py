#!/usr/bin/python3
""" script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
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

    state_add = State(name="Louisiana")
    session.add(state_add)
    session.commit()

    state = session.query(State).filter(State.name == "Louisiana").first()
    print(f"{state.id}")
