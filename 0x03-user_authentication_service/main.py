#!/usr/bin/env python3
"""main.py module"""
from auth import Auth
import requests

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
BASE_URL = "http://127.0.0.1:5000"


def register_user(email: str, password: str) -> None:
    """this function registers a new user"""
    pass


def log_in_wrong_password(email: str, password: str) -> None:
    """represents log_in_wrong_password"""
    pass


def profile_unlogged() -> None:
    """represents profile_unlogged"""
    pass


def log_in(email: str, password: str) -> str:
    """represents log in function"""
    return None


def profile_logged(session_id: str) -> None:
    """represents profile logged function"""
    pass


def log_out(session_id: str) -> None:
    """Logs out the user with the specified session ID."""
    pass


def reset_password_token(email: str) -> str:
    """Requests a password reset token"""
    return None


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Updates the password"""
    pass


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
