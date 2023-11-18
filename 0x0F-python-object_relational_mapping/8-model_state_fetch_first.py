#!/usr/bin/python3
'''
Prints the first State objects from the daabase hbtn_0e_6_usa
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
    try:
        states = session.query(State).order_by(State.id).first()
        print('{}: {}'.format(states.id, states.name))
    except:
        print('Nothing')
