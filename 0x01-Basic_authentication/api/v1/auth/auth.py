#!/usr/bin/env python3

"""
Title: Auth class
Description: this class is the template for all authentication system
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ the authentication class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method that returns false - path & excluded-paths """

        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != "/":
            path += "/"

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ public method that returns none - request """

        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar("User"):
        """ public method that returns none - request : user """

        return None
