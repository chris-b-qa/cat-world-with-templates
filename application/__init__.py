#!/usr/bin/python

from flask import Flask

# Need to initialise application before we import our routes
app = Flask(__name__)

from application import routes
