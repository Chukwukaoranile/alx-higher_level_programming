#!/usr/bin/python3
"""Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    """
    Query the database
    """
    sql = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(sql.format(argv[1],
                                      argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    flag = 0
    for id, name in session.query(State.id, State.name).order_by(State.id):
        if name == argv[4]:
            print(id)
            flag = 1
    if flag == 0:
        print("Not found")
    session.close()
