#!/usr/bin/env python3

"""
Title: Basic Authentication
Description: method extract_base64_authorization_header in the class BasicAuth
that returns the Base64 part of the Authorization header for a
Basic Authentication:
    Return None if authorization_header is None
    Return None if authorization_header is not a string
    Return None if authorization_header doesnt start by Basic
        (with a space at the end)
    Otherwise, return the value after Basic (after the space)
"""

from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
import base64


class BasicAuth(Auth):
    """ basic authentication class """

    def extract_base64_authorization_header(self, ath_h: str) -> str:
        """ method that returns base64 part of the authorization """

        if not ath_h or type(ath_h) != str or not ath_h.startswith("Basic "):
            return
        return "".join(ath_h.split(" ")[1:])

    def decode_base64_authorization_header(self, b64: str) -> str:
        """ method that decodes base64 authorization """

        if not b64 or type(b64) != str:
            return
        try:
            b64_bytes = b64.encode('utf-8')
            res = base64.b64decode(b64_bytes)
            return res.decode('utf-8')
        except Exception:
            return

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user method """

        header = self.authorization_header(request)
        b64header = self.extract_base64_authorization_header(header)
        decoded = self.decode_base64_authorization_header(b64header)
        user_creds = self.extract_user_credentials(decoded)

        return self.user_object_from_credentials(*user_creds)

    def extract_user_credentials(self, db64: str) -> (str, str):
        """ method that returns user credentials """

        if not db64 or type(db64) != str or ":" not in db64:
            return (None, None)
        part_1, part_2 = db64.split(':')[0], "".join(db64.split(':', 1)[1:])
        return (part_1, part_2)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ method that returns user object from credentials """

        if (not user_email or
                type(user_email) != str or
                not user_pwd or type(user_pwd) != str):
            return
        user = None
        # checking for exception
        try:
            user = User.search({"email": user_email})
        except Exception:
            return
        if not user:
            return
        for x in user:
            if x.is_valid_password(user_pwd):
                return x
