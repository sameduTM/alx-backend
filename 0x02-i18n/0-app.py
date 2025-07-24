#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config:
    """Class to configure available languages in app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """basic index route"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
