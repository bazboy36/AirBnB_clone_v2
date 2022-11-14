#!/usr/bin/python3
""" The module for different pages with Flask framework """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ Function that closes the storage"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """Lists all the states"""
    return render_template('9-states.html', states=storage.all(State).values())


@app.route('/states/<id>', strict_slashes=False)
def cities_in_state(id):
    """Lists all the cities in the given state id"""
    states = storage.all(State).values()
    state = None
    for obj in states:
        if id == obj.id:
            state = obj
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
