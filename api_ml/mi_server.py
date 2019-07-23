"""Creando un servidor Flask
"""

from flask import Flask

app = Flask(__name__)

@app.route('/users/<string:nombre>')
def hello_world(nombre=None):

	return ("Hola {}!".format(nombre))

