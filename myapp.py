from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sq

#Build app
app = Flask(__name__)
app.config.from_pyfile('config.py')


#Load local database
db = SQLAlchemy(app)
#db = sq.connect('F:/Projects/GHI/Forecast/temp.db')


#Landing page
@app.route('/')
def landing():
	return render_template('landing.html')


if __name__ == '__main__':
	app.run()