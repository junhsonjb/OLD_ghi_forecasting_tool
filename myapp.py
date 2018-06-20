from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sq


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
#db = sq.connect('F:/Projects/GHI/Forecast/temp.db')

from views import *

if __name__ == '__main__':
	app.run()