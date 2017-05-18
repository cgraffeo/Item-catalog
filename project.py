from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, State, Park, User
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
    states = session.query(State).order_by(asc(State.name))
    return render_template('states.html', states=states)

@app.route('/state/<int:state_id>/parks')
def typeList(state_id):
    states = session.query(State).filter_by(id=state_id).one()
    parks = session.query(Park).filter_by(state_id=state_id).all()
    return render_template('parklist.html', parks=parks, state_id=state_id, states=states)

@app.route('/parks/new', methods=['GET', 'POST'])
def newPark():
    newPark = Park(name=request.form['name'], description=request.form['description'], photo=request.form['photo'], park_type=request.form['park_type'])
    session.add(newPark)
    session.commit()
    return render_template('newpark.html')

@app.route('/<int:park_id>/details')
def parkDetail(park_id):
    park = session.query(Park).filter_by(id=park_id).one()
    return render_template('parkdetail.html', park_id=park_id)

@app.route('/<int:park_id>/edit')
def editPark(park_id, methods=['GET', 'POST']):
    editPark = session.query(Park).filter_by(id=park_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editPark.name = request.form['name']
        if request.form['description']:
            editPark.description = request.form['description']
        if request.form['photo']:
            editPark.photo = request.form['photo']
        if reuqest.form['park_type']:
            editPark.park_type = request.form['park_type']
        session.add(editPark)
        session.commit()
    return render_template('editpark.html', park_id=park_id)

@app.route('/<int:park_id>/delete', methods=['GET', 'POST'])
def deletePark(park_id):
    parkToDelete = session.query(Park).filter_by(id=park_id).one()
    if request.method == 'POST':
        session.delete(parkToDelete)
        session.commit()
    return render_template('deletepark.html', park_id=park_id)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
