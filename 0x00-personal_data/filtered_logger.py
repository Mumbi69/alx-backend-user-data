#!/usr/bin/env python3
"""Regex-ing"""

import re


def filter_datum(fields, redaction, message, separator):
    """function named filter_datum which takes four arguments"""
    return (re.sub(rf"({'|'.join(fields)})=.*?{separator}",
            rf"\1={redaction}{separator}", message))
