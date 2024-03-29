#!/usr/bin/python3
"""Write a script that lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    """
    Conecting and quering the database from the code base
    """
    sql = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(sql.format(argv[1],
                                      argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    for id, name in session.query(State.id, State.name).order_by(State.id):
        print("{}: {}".format(id, name))
    session.close()
