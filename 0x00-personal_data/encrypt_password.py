#!/usr/bin/env python3

"""
Title: Encrypting password
Description: Implement a hash_password function that expects one string
argument name password and returns a salted, hashed password,
which is a byte string.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ fxn that generates a salted and hashed password """

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ fxn that validates the provided passwd maching the hashed passwd """

    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
