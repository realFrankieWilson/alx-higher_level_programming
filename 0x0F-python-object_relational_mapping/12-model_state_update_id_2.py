#!/usr/bin/python3
'''
A script that adds the State object "Louisina" to the database hbtn_0e_6_usa
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

    obj = State(name='Louisiana')
    session.add(obj)
    session.commit()

    print(obj)
