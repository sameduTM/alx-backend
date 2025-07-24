#!/usr/bin/env python3
"""Basic Babel setup"""
from flask_babel import Babel
app = __import__('0-app').app


class Config:
    """configure available languages, locale and timezone in app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)
