#!/usr/bin/python3
""" Defines the message on hbnb page """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Function that returns the message for the index """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns the message for /hbnb """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
