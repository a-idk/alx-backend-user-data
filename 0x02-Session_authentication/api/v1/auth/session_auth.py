#!/usr/bin/env python3

"""
Title: Session Authentication
Description: script that gets session authentication module for the API.
"""

from flask import request
from .auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """ Class Session authentication """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Function that creates session id for user """
        if isinstance(user_id, str):
            sess_id = str(uuid4())
            self.user_id_by_session_id[sess_id] = user_id
            return sess_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Function that retrieves user id of user with given session id """
        if isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None) -> User:
        """ Function that retrieves user with request """
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        if user_id:
            return User.get(user_id)
        return None

    def destroy_session(self, request=None):
        """ Function that destroys an authenticated session """
        sess_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(sess_id)
        if (request is None or sess_id is None) or user_id is None:
            return False
        if sess_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[sess_id]
        return True
