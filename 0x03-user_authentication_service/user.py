#!/usr/bin/env python3

"""
Title: User model
Description: create a SQLAlchemy model named User for a database table
named users (by using the mapping declaration of SQLAlchemy).

The model will have the following attributes:
- id, the integer primary key
- email, a non-nullable string
- hashed_password, a non-nullable string
- session_id, a nullable string
- reset_token, a nullable string
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """ User class base model """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self):
        """ methd that returns the String representation """
        return f"User: id={self.id}"
