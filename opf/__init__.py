from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from flask_session import Session
from flask_principal import Principal

db = SQLAlchemy()
login_manager = LoginManager()
principal = Principal()
#sess = Session()

def create_app():
	app = Flask(__name__)
	app.config.from_object('config.Config')

	# Initialize Plugins
	db.init_app(app)
	login_manager.init_app(app)
	principal.init_app(app)
	#sess.init_app(app)

	with app.app_context():
		from . import view
		from . import auth

		db.init_app(app)
		login_manager.init_app(app)
		principal.init_app(app)

		app.register_blueprint(view.main_bp)
		app.register_blueprint(auth.auth_bp)

	return app
