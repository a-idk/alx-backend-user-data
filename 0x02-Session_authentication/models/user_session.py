#!/usr/bin/env python3

"""
Title: User session model
Description: user session class
"""

from models.base import Base


class UserSession(Base):
    """ Class User session """

    def __init__(self, *args: list, **kwargs: dict):
        """ Initializing user session """

        super().__init__(*args, **kwargs)

        self.user_id = kwargs.get('user_id')

        self.session_id = kwargs.get('session_id')
