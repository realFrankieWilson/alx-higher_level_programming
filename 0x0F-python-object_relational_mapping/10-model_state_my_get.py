#!/usr/bin/python3
'''
Prints the State object that contain the name
passed as argument
from  the daabase hbtn_0e_6_usa
'''
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3], pool_pre_ping=True)
            )
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == argv[4]).first()
    if not states:
        print('Not found')
    else:
        print(states.id)
