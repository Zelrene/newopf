from flask import Flask, Blueprint, abort, render_template, request, flash, session, url_for

from flask_login import login_user, login_required, current_user
from src import UserController

# Blueprint Configuration
error_bp = Blueprint(
	"error_bp", __name__,
	template_folder='templates',
	static_folder='static'
)

@error_bp.errorhandler(400)
def page_not_found(e):
	session['redirected_from'] = request.url
	title = 'Bad Directory'
	message = 'The page you are trying to access is unavailable. The page that directed you here should not have made a link to this page.'
	return render_template('page_not_found.html', title=title, message=message, show=True)

@error_bp.errorhandler(401)
def page_not_found(e):
	session['redirected_from'] = request.url
	title = 'Unauthorized Page'
	message = 'The page you are trying to access is unavailable. You lack the valid authentication credentials to view this page.'
	return render_template('page_not_found.html', title=title, message=message, show=False)

@error_bp.errorhandler(403)
def page_not_found(e):
	session['redirected_from'] = request.url
	title = 'Forbidden Page'
	message = 'The page you are trying to access is unavailable. You lack the valid authentication credentials to view this page.'
	return render_template('page_not_found.html', title=title, message=message, show=True)

@error_bp.errorhandler(404)
def page_not_found(e):
	session['redirected_from'] = request.url
	title = 'Sorry, Page Not Found'
	message = 'The page you requested does not exist. You may have followed a bad link, or the page may have been moved or removed.'
	return render_template('page_not_found.html', title=title, message=message, show=True)