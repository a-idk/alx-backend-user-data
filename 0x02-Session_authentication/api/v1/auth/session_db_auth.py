#!/usr/bin/env python3

"""
Title: Session authentication Database
Description: Session authentication with storage module for API
"""

from flask import request
from datetime import datetime, timedelta
from models.user_session import UserSession
from .session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """ Class Session authentication Database """

    def create_session(self, user_id=None) -> str:
        """ method that creates & stores session id for user """

        session_id = super().create_session(user_id)

        if type(session_id) == str:
            kwargs = {
                'user_id': user_id,
                'session_id': session_id,
            }

            user_session = UserSession(**kwargs)
            user_session.save()
            return session_id

    def user_id_for_session_id(self, session_id=None):
        """ mthd that retrieves user id of user with given session id """

        try:
            sessions = UserSession.search({'session_id': session_id})

        except Exception:
            return None

        # check
        if len(sessions) <= 0:
            return None

        current_time = datetime.now()
        t_span = timedelta(seconds=self.session_duration)
        expire_time = t_span + sessions[0].created_at

        if expire_time < current_time:
            return None

        return sessions[0].user_id

    def destroy_session(self, request=None) -> bool:
        """ mthd that destroys authenticated session """

        session_id = self.session_cookie(request)

        try:
            sessions = UserSession.search({'session_id': session_id})

        except Exception:
            return False

        if len(sessions) <= 0:
            return False

        sessions[0].remove()

        return True
