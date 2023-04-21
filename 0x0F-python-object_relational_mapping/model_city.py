#!/usr/bin/python3
"""a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa"""
from sqlalchemy import Column, Integer, String
from model_state import Base
from sqlalchemy import ForeignKey


class City(Base):
    """inherits from Base (imported from model_state)"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
