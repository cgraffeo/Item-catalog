from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, State, ParkType, Park, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///parks.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
@app.route('/login')
def showlogin():
    return "This page will show login"

@app.route('/')
@app.route('/state')
def stateList():
    return "This page will show a list of states"

@app.route('/state/<int:state_id>/type')
def typeList():
    return "This page will show a list of types of parks"

@app.route('/state/<int:state_id>/type/<int:type_id>')
def parkList():
    return "This page will show a list of parks of a type"

@app.route('/state/<int:state_id>/type/<int:type_id>/new')
def newPark():
    return "This page will allow you to create a new park"

@app.route('/state/<int:state_id>/type/<int:type_id>/<int:park_id>')
def parkDetail():
    return "This page will show a specific park and it's details"

@app.route('/state/<int:state_id>/type/<int:type_id>/<int:park_id>/edit')
def editPark():
    return "This page will allow you to edit a specific park details"

@app.route('/state/<int:state_id>/type/<int:type_id>/<int:park_id>/delete')
def deletePark():
    return "This page will allow you to delete a specific park"

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
