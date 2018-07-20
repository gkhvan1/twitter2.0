import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'twitter.db'
CSRF_ENABLED = True
SECRET_KEY = 'my_precious'
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
