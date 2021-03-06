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
    
    # Mail config
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'newopf@gmail.com'
    MAIL_PASSWORD = 'passOpf@985'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    #phone number config
    VONAGE_API_KEY = 'd576fb48'
    VONAGE_API_SECRET = 'l28b1nI0Opk2ujtJ'
    VONAGE_API_SECRET_SIGN = 'BYzr4KcMg8TMRAfXgfSTxjHy87lCRp5PbjI3bljdhXDiF5gxgr'

    '''
    vonage_client = vonage.Client(
    key = VONAGE_API_KEY,
    secret = VONAGE_API_SECRET,
    signature_secret = VONAGE_API_SECRET_SIGN
    )
    '''













