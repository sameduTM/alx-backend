#!/usr/bin/env python3
"""Get locale from request"""
from flask import request

app = __import__("1-app").app
babel = __import__('1-app').babel


@babel.localeselector
def get_locale():
    """method to determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])
