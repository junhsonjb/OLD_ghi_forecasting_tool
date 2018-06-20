import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///F:\\Projects\\GHI\\Forecast\\Forecast.db'
SECRET_KEY = os.urandom(24)
SQLALCHEMY_TRACK_MODIFICATIONS = False