#!/usr/bin/env python3
"""Basic auth module"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Represents the class Basic Auth"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """extract_base64_authorization_header"""
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]
