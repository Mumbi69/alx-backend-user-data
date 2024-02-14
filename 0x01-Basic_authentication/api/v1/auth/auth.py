#!/usr/bin/env python3
"""authentication module"""

from flask import Flask, request
from typing import List, TypeVar


class Auth:
    """represents the class authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """function auth"""
        return False


    def authorization_header(self, request=None) -> str:
        """function authentication header"""
        return None


    def current_user(self, request=None) -> TypeVar("User"):
        """function current user"""
        return None

