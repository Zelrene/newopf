from flask import Blueprint, redirect, render_template, flash, request, session, url_for, current_app

from flask_login import login_user, login_required, current_user, logout_user

from werkzeug.security import generate_password_hash, check_password_hash

from flask_principal import Permission, Identity, AnonymousIdentity
from flask_principal import RoleNeed, UserNeed, identity_loaded, identity_changed

from . import login_manager, principal
from src import UserController, TicketController

# Blueprint Configuration
auth_bp = Blueprint(
	'auth_bp', __name__,
	template_folder='templates',
	static_folder='static'
)

admin_permission = Permission(RoleNeed('Admin'))
student_permission = Permission(RoleNeed('Student'))

ticket_controller = TicketController.TicketController()
user_controller = UserController.UserController()

from src.models.user import User

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

# Flask-Principal: Add the Needs that this user can 
# Updates Role and User Needs
@identity_loaded.connect
def on_identity_loaded(sender, identity):
	# Set the identity user object
	identity.user = current_user

	# Add the UserNeed to the identity (We are not using UserNeed here)
	if hasattr(current_user, 'id'):
		identity.provides.add(UserNeed(current_user.id))

	if hasattr(current_user, 'user_role'):
		#for role in current_user.roles:
		identity.provides.add(RoleNeed(current_user.user_role))




@auth_bp.route('/log_in.html', methods=['GET', 'POST'])
def log_in():
	if request.method == 'GET':
		return render_template(url_for('auth_bp.log_in'))

	if request.method == 'POST':
		if request.form['submit_btn'] == 'Sign Up':
			return redirect(url_for('auth_bp.sign_up'))

		net_id = request.form['Net_Id']
		password = request.form['Password']
		
		user = user_controller.get_user_info_with_matching_netid(net_id)
		
		if not user or not check_password_hash(user.password, password):
			flash('Please check your login details and try again.')
			return redirect(url_for('auth_bp.log_in'))

		# If the above check passes, then we know the user has the right credentials
		login_user(user)

		# Update identity of user thus calling
		identity_changed.send(current_app._get_current_object(), identity=Identity(user.net_id))

		return redirect(url_for('main_bp.dashboard'))

@auth_bp.route('/sign_up.html', methods=['GET', 'POST'])
def sign_up():
	if request.method == 'GET':
		return render_template(url_for('auth_bp.sign_up'))

	if request.method == 'POST':
		if request.form['submit_btn'] == 'Log In':
			return redirect(url_for('auth_bp.log_in'))

		first_name = request.form['First_Name']
		last_name = request.form['Last_Name']
		contact_email= request.form['Contact_Email']
		net_id = request.form['Net_Id']
		password = request.form['Password']

		user_n = user_controller.get_user_info_with_matching_netid(net_id)
		user_e = user_controller.get_user_info_with_matching_email(contact_email)

		# Error Message for Sign Up
		if not request.form.get('User_Role') or	not request.form.get('Gender') or not request.form.get('Year') or not first_name or not last_name or not contact_email or not password:
			flash('Not all fields are filled. Please complete all required fields before signing up.')

			if net_id and user_n:
				flash('A user with the same NETID already exists. Please use a different NETID.')
			
			if contact_email and user_e:
				flash('A user with the email already exists. Please use a different email.')

			return redirect(url_for('auth_bp.sign_up'))

		user_role = request.form['User_Role']
		gender = request.form['Gender']
		student_year = request.form['Year']

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
			
		return redirect(url_for('auth_bp.log_in'))