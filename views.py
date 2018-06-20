from myapp import app
from logic import country
from models import Member
from forms import LoginForm
from flask import render_template, session, request, redirect, url_for, g

@app.route('/')
def index():
	firstMember = Member.query.first()
	session['user'] = firstMember.name
	return '<h1> You are on the index!' + country + '</h1><br/><h2> The first member is: ' + firstMember.name + '</h2>'

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session.pop('user', None)

		if request.form['password'] == 'password':
			session['user'] = request.form['username']
			return redirect(url_for('protected'))

	form = LoginForm()
	return render_template('index.html', form=form)

@app.route('/protected')
def protected():
	if g.user:
		return render_template('protected.html')

	return redirect(url_for('login'))

@app.before_request
def before_request():
	g.user = None
	if 'user' in session:
		g.user = session['user']

@app.route('/getsession')
def getsession():
	if 'user' in session:
		return session['user']

	return 'Not logged in!'

@app.route('/dropsession')
def dropsession():
	session.pop('user', None)
	return 'Dropped!'