#!/usr/bin/env python3
"""Regexing"""

import logging
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    This function uses regular expressions (re.sub) to
    search for occurrences of specified fields in the log
    message and replace them with the specified redaction.
    """
    return (re.sub(rf"({'|'.join(fields)})=.*?{separator}",
            rf"\1={redaction}{separator}", message))


class RedactingFormatter(logging.Formatter):
    """
    This class defines a custom log format where certain
    fields are obfuscated using the filter_datum function.
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initializing class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """This is a format function """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return (super().format(record))
