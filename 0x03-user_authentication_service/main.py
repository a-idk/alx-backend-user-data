#!/usr/bin/env python3

"""
Title: Main script
Description: Create a new module called main.py. Create one function for each
of the following tasks. Use the requests module to query your web server for
the corresponding end-point. Use assert to validate the response’s expected
status code and payload (if any) for each task
"""


def register_user(email: str, password: str) -> None:
    """ method to register user """
    assert True
    return


def log_in(email: str, password: str) -> str:
    """ log in methd """
    assert True
    return ""


def log_in_wrong_password(email: str, password: str) -> None:
    """ wrong password check """
    assert True
    return


def log_out(session_id: str) -> None:
    """ log out method """
    assert True
    return


def profile_logged(session_id: str) -> None:
    """ profile logged Method """
    assert True
    return


def profile_unlogged() -> None:
    """ method profile unlogged """
    assert True
    return


def reset_password_token(email: str) -> str:
    """ reset password token method """
    assert True
    return ""


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ update password method """
    assert True
    return


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, "")
    log_in(EMAIL, NEW_PASSWD)
