#!/usr/bin/python3
""" The module for different pages with Flask framework """

from flask import Flask, request, render_template
from models.state import State
from models import storage


app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close(exception):
    """ Function that closes the storage"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    """ Lists all the states """
    return render_template('7-states_list.html', states=storage.all(State))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
