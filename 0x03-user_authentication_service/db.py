#!/usr/bin/env python3

"""
Title: DB module
Description: DB class provided below to implement the add_user method
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User
from typing import TypeVar


VALID_FIELDS = [
        'id',
        'email',
        'hashed_password',
        'session_id',
        'reset_token'
        ]


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ _session method """

        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()

        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ add_user method """

        if not email or not hashed_password:
            return

        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ find user method """

        if not kwargs or any(i not in VALID_FIELDS for i in kwargs):
            raise InvalidRequestError
        session = self._session
        try:
            return session.query(User).filter_by(**kwargs).one()
        except Exception:
            raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """ user update method """

        session = self._session
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if key not in VALID_FIELDS:
                raise ValueError
            setattr(user, key, value)

        session.commit()
