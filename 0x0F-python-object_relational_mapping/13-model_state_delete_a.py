#!/usr/bin/python3
'''
A script that changes the name object from database hbtn_0e_6_usa
'''
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3])
            )
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))
    for state in states.all():
        session.delete(state)
    session.commit()

    session.close()
