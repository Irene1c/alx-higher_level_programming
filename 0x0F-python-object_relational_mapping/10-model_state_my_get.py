#!/usr/bin/python3
"""script that prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv, exit


if __name__ == "__main__":
    if len(argv) < 5:
        exit()

    username = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]

    if not name.isalpha():
        exit()

    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
            @localhost:3306/{database}', pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    States = session.query(State).filter(State.name == name).first()
    if States:
        print(f"{States.id}")
    else:
        print("Not found")
