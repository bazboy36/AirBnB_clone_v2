#!/usr/bin/python3
""" The module for different pages with Flask framework """

from flask import Flask
from flask import render_template


app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


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


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_number(n):
    """Function that returns a template"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """ Function which tells if the number is odd or even"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
