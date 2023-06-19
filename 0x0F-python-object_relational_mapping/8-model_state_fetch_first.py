#!/usr/bin/python3
"""  script that prints the first State object from the database hbtn_0e_6_usa"""
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

    States = session.query(State).order_by(State.id).first()
    if States:
        print(f"{States.id}: {States.name}")
    else:
        print()
