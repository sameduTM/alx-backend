#!/usr/bin/env python3
"""Parametrize templates"""
import flask
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)


class Config:
    """configures available languages in app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """returns a user dictionary or None if the ID cannot be found or
        if login_as was not passed.
    """
    _id = request.args.get('login_as')
    if not _id or int(_id) not in users.keys():
        return None
    return users[int(_id)]


@app.before_request
def before_request():
    """find a user if any and set it as a global on flask.g.user"""
    flask.g.user = get_user()


@babel.localeselector
def get_locale():
    """determine best match with supported languages"""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return request.args.get('locale')
    if get_user():
        return request.args.get(get_user()["locale"])  # type: ignore
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """default route"""
    return render_template('5-index.html', get_user=get_user)


if __name__ == "__main__":
    app.run(debug=True)
