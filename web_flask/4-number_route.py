#!/usr/bin/python3
""" Definines the message on the /number page """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Returns the message for the index """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns the message for /hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def message_c(text):
    """ Returns a custom message for c """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def message_python(text='is cool'):
    """ Returns a custom message for python """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def message_number(n):
    """ Returns a custom message for /number """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
