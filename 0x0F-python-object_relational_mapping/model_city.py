#!/usr/bin/python3
"""Model for State class"""

from model_state import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeingKey, MetaData

Base = declarative_base()


class City(Base):
    """Class city"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeingKey('state.id'), nullable=False)
