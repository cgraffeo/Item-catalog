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

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Park Finder (Udacity Item-Catalog project)"

# Connect to Database and create database session
engine = create_engine('sqlite:///parks.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)

@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

# User Helper Functions


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None
    # DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session['access_token']
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return redirect(url_for('stateList'))
    else:

        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

# JSON APIs to view Park Information
@app.route('/state/<int:state_id>/parks/JSON')
def parkListJSON(state_id):
    states = session.query(State).filter_by(id=state_id).one()
    parks = session.query(Park).filter_by(state_id=state_id).all()
    return jsonify(Parks=[park.serialize for park in parks])

@app.route('/<int:park_id>/details/JSON')
def parkJSON(park_id):
    parks = session.query(Park).filter_by(id=park_id).one()
    return jsonify(Park=parks.serialize)


@app.route('/state/JSON')
def statesJSON():
    states = session.query(State).all()
    return jsonify(states=[state.serialize for state in states])

@app.route('/')
@app.route('/state')
def stateList():
    states = session.query(State).order_by(asc(State.name))
    return render_template('states.html', states=states)

@app.route('/state/<int:state_id>/parks')
def typeList(state_id):
    states = session.query(State).filter_by(id=state_id).one()
    parks = session.query(Park).filter_by(state_id=state_id).all()
    return render_template('parklist.html', parks=parks, state_id=state_id,
                           states=states)

@app.route('/parks/new', methods=['GET', 'POST'])
def newPark():
    if request.method == 'POST':
        addPark = Park(name=request.form['name'], description=request.form['description'], photo=request.form['photo'], park_type=request.form['park_type'], state_id=request.form['state_id'])
        session.add(addPark)
        session.commit()
        description = request.form['description']
        park = session.query(Park).filter_by(description=description).one()
        return redirect(url_for('parkDetail', park_id=park.id))
    else:
        return render_template('newpark.html')

@app.route('/<int:park_id>/details')
def parkDetail(park_id):
    park = session.query(Park).filter_by(id=park_id).one()
    return render_template('parkdetail.html', park=park, park_id=park_id)

@app.route('/<int:park_id>/edit', methods=['GET', 'POST'])
def editPark(park_id):
    editPark = session.query(Park).filter_by(id=park_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editPark.name = request.form['name']
        if request.form['description']:
            editPark.description = request.form['description']
        if request.form['photo']:
            editPark.photo = request.form['photo']
        if request.form['park_type']:
            editPark.park_type = request.form['park_type']
        if request.form['state_id']:
            editPark.state_id = request.form['state_id']
        session.add(editPark)
        session.commit()
        return redirect(url_for('parkDetail', park_id=park_id, editPark=editPark))
    else:
        return render_template('editpark.html', editPark=editPark, park_id=park_id)

@app.route('/<int:park_id>/delete', methods=['GET', 'POST'])
def deletePark(park_id):
    parkToDelete = session.query(Park).filter_by(id=park_id).one()
    if request.method == 'POST':
        session.delete(parkToDelete)
        session.commit()
        return redirect('/')
    else:
        return render_template('deletepark.html', park_id=park_id, park=parkToDelete)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
