#!/usr/bin/env python3
"""Get locale from request"""
from flask import request

babel = __import__('1-app').babel
Config = __import__('1-app').Config


@babel.localeselector
def get_locale():
    """method to determine the best match with our supported languages"""
    return request.accept_languages.best_match(Config.LANGUAGES)
