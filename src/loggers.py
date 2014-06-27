"""
Helper functions for configuring loggers.
"""

import logging

from .config import app_config

def get_stderr_handler(format_string, level):
    "Returns a standard error handler with provided format and level"
    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(*format_string))
    return handler

def get_app_stderr_handler():
    "Returns a configured stderr_handler"
    return get_stderr_handler(app_config.STDERR_LOG_FORMAT, app_config.APP_LOG_LEVEL)
