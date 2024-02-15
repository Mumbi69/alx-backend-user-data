#!/usr/bin/env python3
"""authentication module"""

from flask import Flask, request
from typing import List, TypeVar


class Auth:
    """represents the class authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """function auth"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """function authentication header"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar("User"):
        """function current user"""
        return None
