#!/usr/bin/env python3
"""Parametrize templates"""
from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import (
    Babel,
    _,
    gettext
)

app = Flask(__name__)


class Config:
    """configures available languages in app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """determine best match with supported languages"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """default route"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
