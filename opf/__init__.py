from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from flask_session import Session
from flask_principal import Principal
from flask_mail import Mail
from vonage import vonage, Sms


db = SQLAlchemy()
login_manager = LoginManager()
principal = Principal()
mail = Mail()
vonage_client = vonage.Client(
	key = 'd576fb48',
	secret = 'l28b1nI0Opk2ujtJ',
	signature_secret = 'BYzr4KcMg8TMRAfXgfSTxjHy87lCRp5PbjI3bljdhXDiF5gxgr'
)
sms = vonage.Sms(vonage_client)
#sess = Session()

def create_app():
	app = Flask(__name__)
	app.config.from_object('config.Config')

	# Initialize Plugins
	db.init_app(app)
	login_manager.init_app(app)
	principal.init_app(app)
	mail.init_app(app)
	#sess.init_app(app)

	with app.app_context():
		from . import view
		from . import auth
		from . import error

		db.init_app(app)
		login_manager.init_app(app)
		principal.init_app(app)
		mail.init_app(app)

		app.register_blueprint(view.main_bp)
		app.register_blueprint(auth.auth_bp)
		app.register_blueprint(error.error_bp)

	return app
