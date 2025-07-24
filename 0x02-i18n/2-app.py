#!/usr/bin/env python3
"""Get locale from request"""
from flask import g, request

babel = __import__('1-app').babel
config = __import__('1-app').Config


@babel.localeselector
def get_locale():
    """method to determine the best match with our supported languages"""
    return request.accept_languages.best_match(config.LANGUAGES)
