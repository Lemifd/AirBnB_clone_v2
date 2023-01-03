#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page with a list of all states and related cities.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(reponse_or_exc):
    """runs this method when app context tears down"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states_list():
    """Flask web application that displays <states.id>, <states.name> with
associated <cities.id>, <cities.name> at route:'/cities_by_states' """
    state_dict = storage.all(State)
    return render_template('8-cities_by_states.html', state_dict=state_dict)


if __name__ == "__main__":
    app.run()
