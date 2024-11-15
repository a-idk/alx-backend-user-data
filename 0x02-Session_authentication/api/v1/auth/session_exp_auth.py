#!/usr/bin/env python3

"""
Title: Session authentication expiration
Description: expiration module for session authentication for the API.
"""

import os
from flask import request
from datetime import datetime, timedelta
from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """ Class Session authentication expiration """

    def __init__(self) -> None:
        """ Initializing """

        super().__init__()

        try:
            self.session_duration = int(os.getenv('SESSION_DURATION', '0'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ fxn that creates session id for user """

        sess_id = super().create_session(user_id)

        # checking for string
        if type(sess_id) != str:
            return None

        self.user_id_by_session_id[sess_id] = {
            'user_id': user_id,
            'created_at': datetime.now(),
        }
        return sess_id

    def user_id_for_session_id(self, session_id=None) -> str:
        """ mthd that retrieves user id of user with given session id """

        if session_id in self.user_id_by_session_id:
            session_dict = self.user_id_by_session_id[session_id]

            if self.session_duration <= 0:
                return session_dict['user_id']

            if 'created_at' not in session_dict:
                return None

            current_time = datetime.now()
            t_span = timedelta(seconds=self.session_duration)
            expire_time = t_span + session_dict['created_at']

            if expire_time < current_time:
                return None

            return session_dict['user_id']
