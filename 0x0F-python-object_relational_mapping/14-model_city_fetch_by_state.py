#!/usr/bin/python3
"""a Python file similar to model_state.py named model_city.py that contains the class definition of a City"""
from model_city import City
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    """
    Conecting to MySQL database
    """
    sql = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(sql.format(argv[1],
                                      argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    for s, c in session.query(State, City).\
            order_by(City.id).\
            filter(City.state_id == State.id).\
            all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
