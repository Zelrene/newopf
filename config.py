from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    # General Config
    SECRET_KEY = 'secret-key-goes-here'
    DEBUG = True
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Flask-SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db' 
    