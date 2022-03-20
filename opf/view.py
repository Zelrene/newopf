from unicodedata import name
from flask import Flask, Blueprint, abort, render_template, request, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, login_user, login_required, current_user, logout_user

from flask_principal import Principal, Permission, Identity, AnonymousIdentity
from flask_principal import RoleNeed, UserNeed, identity_loaded, identity_changed

from opf import app

#app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret-key-goes-here'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

#admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")

from src.models.user import User

# Login Functionality
login_manager = LoginManager()
login_manager.login_view = '/log_in.html'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

# Authorization Functionality
principal = Principal()
principal.init_app(app)

# Flask-Principal: Create a permission with a single RoleNeed
admin_permission = Permission(RoleNeed('Admin'))
student_permission = Permission(RoleNeed('Student'))

# Flask-Principal: Add the Needs that this user can 
# Updates Role and User Needs
@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
	# Set the identity user object
	identity.user = current_user

	# Add the UserNeed to the identity (We are not using UserNeed here)
	if hasattr(current_user, 'id'):
		identity.provides.add(UserNeed(current_user.id))

	if hasattr(current_user, 'user_role'):
		#for role in current_user.roles:
		identity.provides.add(RoleNeed(current_user.user_role))
 


from src import TicketController, UserController

ticket_controller = TicketController.TicketController()
user_controller = UserController.UserController()

@app.route('/')
def index():
	return redirect('/log_in.html')

@app.route('/log_in.html', methods = ['GET', 'POST'])
def log_in():
	if request.method == 'GET':
		return render_template('log_in.html')

	if request.method == 'POST':
		if request.form['submit_btn'] == 'Sign Up':
			return redirect('sign_up.html')

		net_id = request.form['Net_Id']
		password = request.form['Password']
		
		user = user_controller.get_user_info_with_matching_netid(net_id)
		
		if not user or not check_password_hash(user.password, password):
			flash('Please check your login details and try again.')
			return redirect('log_in.html')

		# If the above check passes, then we know the user has the right credentials
		login_user(user)

		# Update identity of user thus calling
		identity_changed.send(app, identity=Identity(user.net_id))

		return redirect('/dashboard.html')

@app.route('/sign_up.html', methods = ['GET', 'POST'])
def sign_up():
	if request.method == 'GET':
		return render_template('sign_up.html')

	if request.method == 'POST':
		if request.form['submit_btn'] == 'Log In':
			return redirect('log_in.html')

		first_name = request.form['First_Name']
		last_name = request.form['Last_Name']
		user_role = request.form['User_Role']
		contact_email= request.form['Contact_Email']
		net_id = request.form['Net_Id']
		gender = request.form['Gender']
		student_year = request.form['Year']
		password = request.form['Password']

		user_n = user_controller.get_user_info_with_matching_netid(net_id)
		user_e = user_controller.get_user_info_with_matching_email(contact_email)

		# Error Message for Sign Up
		if not first_name or not last_name or not contact_email or not password:
			flash('Not all fields are filled. Please complete all required fields before signing up.')

			if net_id and user_n:
				flash('A user with the same NETID already exists. Please use a different NETID.')
			
			if contact_email and user_e:
				flash('A user with the email already exists. Please use a different email.')

			return redirect('/sign_up.html')

		user_controller.create_user( 
			first_name = first_name,
			last_name = last_name,
			user_role = user_role,
			contact_email = contact_email,
			net_id = net_id,
			gender = gender,
			student_year = student_year,
			password = generate_password_hash(password)
			)
			
		return redirect('/log_in.html')


@app.route('/create_tickets.html', methods = ['GET', 'POST'])
@login_required
def create_tickets():
	if request.method == 'GET':
		curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
		return render_template('create_tickets.html', name=curr_user_name)
	
	if request.method == 'POST':
		title = request.form['Title']
		description = request.form['Description']
		location = request.form['Location']
		building = request.form['Building']
		severity_level = request.form['Severity_level']
		unit = request.form['Unit#']
		contact = request.form['Contact']
		additonalNotes = request.form['AdditionalNotes']
		status = "pending"
		creator_id = 1234
		
		if not title or not description or not location or not building or not unit or not contact:
			flash('Not all required fields are filled. Please fill all required fields before submitting your ticket.')
			return redirect('create_tickets.html')

		ticket_controller.create_ticket(
			title = title,
			description = description, 
			location = location,
			building = building,
			severity_level = severity_level,
			unit = unit,
			contact = contact,
			additionalNotes = additonalNotes,
			status = status,
			creator_id = creator_id)

		role = user_controller.get_role_with_matching_netid(current_user.net_id)

		if role == 'Admin':
			return redirect('/view_tickets.html')
		else:
			return redirect('/view_single_ticket.html')

@app.route('/view_tickets.html')
@login_required
@admin_permission.require(http_exception=403)
def view_tickets():
	tickets = []
	tickets = ticket_controller.get_tickets()
	curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
	return render_template('view_tickets.html', tickets=tickets, name=curr_user_name)

@app.route('/view_single_ticket.html')
@login_required
@student_permission.require(http_exception=403)
def view_single_ticket():
	curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
	return render_template('view_single_ticket.html', name=curr_user_name)

@app.route('/dashboard.html')
@login_required
def dashboard():
	curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
	return render_template('dashboard.html', name=curr_user_name)

@app.route('/faq.html')
@login_required
def faq():
	curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
	return render_template('faq.html', name=curr_user_name)

	
@app.route('/log_out')
@login_required
def log_out():
	logout_user()
	return redirect('/log_in.html')

@app.errorhandler(403)
@login_required
def page_not_found(e):
	session['redirected_from'] = request.url
	curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
	return render_template('page_not_found.html', name=curr_user_name)

#if __name__ == '__main__':
#	app.run()