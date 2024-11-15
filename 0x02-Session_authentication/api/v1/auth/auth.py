#!/usr/bin/env python3

"""
Title: Auth class
Description: this class is the template for all authentication system
"""

from flask import request
from typing import List, TypeVar
import os
import re


class Auth:
    """ the authentication class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method that returns false - path & excluded-paths """

        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != "/":
            path += "/"

        return path not in excluded_paths
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''

                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])

                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])

                else:
                    pattern = '{}/*'.format(exclusion_path)

                if re.match(pattern, path):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ public method that returns none - request """

        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar("User"):
        """ public method that returns none - request : user """

        return None

    def session_cookie(self, request=None) -> str:
        """ mthd that gets the value of the cookie named SESSION_NAME """

        if request is not None:
            cookie_name = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)
