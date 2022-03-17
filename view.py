from unicodedata import name
from flask import Flask, abort, render_template, request, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, login_user, login_required, current_user, logout_user

from flask_principal import Principal, Permission, Identity, AnonymousIdentity
from flask_principal import RoleNeed, UserNeed, identity_loaded, identity_changed


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from src.models.user import User

#login functionality
login_manager = LoginManager()
login_manager.login_view = '/log_in.html'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


principal = Principal()
principal.init_app(app)

# Flask-Principal: Create a permission with a single RoleNeed
admin_permission = Permission(RoleNeed('Admin'))
student_pernission = Permission(RoleNeed('Student'))

# Flask-Principal: Add the Needs that this user can satisfy
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

		#if the above check passes, then we know the user has the right credentials
		login_user(user)

		#identity_changed.send(app, identity=Identity(user.net_id))

		return redirect('dashboard.html')

@app.route('/sign_up.html', methods = ['GET', 'POST'])
def sign_up():
	if request.method == 'GET':
		return render_template('sign_up.html')

	if request.method == 'POST':
		first_name = request.form['First_Name']
		last_name = request.form['Last_Name']
		isStudent = request.form['Is_Student']
		contact_email= request.form['Contact_Email']
		net_id = request.form['Net_Id']
		gender = request.form['Gender']
		student_year = request.form['Year']
		password = request.form['Password']

		user_n = user_controller.get_user_info_with_matching_netid(net_id)
		user_e = user_controller.get_user_info_with_matching_email(contact_email)

		if user_n or user_e:
			flash('A user with the same net_id or email already exists. Please use a different net_id or password.')
			return redirect('sign_up.html')

		user_controller.create_user( first_name = first_name,
		last_name = last_name,
		contact_email = contact_email,
		net_id = net_id,
		gender = gender,
		student_year = student_year,
		password = generate_password_hash(password),
		isStudent = isStudent)

		return render_template('log_in.html')


@app.route('/create_tickets.html', methods = ['GET', 'POST'])
@login_required
def create_tickets():
	if request.method == 'GET':
		return render_template('create_tickets.html')
	
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
		
		ticket_controller.create_ticket(title=title,
		description=description, 
		location=location,
		building=building,
		severity_level=severity_level,
		unit=unit,
		contact=contact,
		additionalNotes=additonalNotes,
		status=status,
		creator_id= creator_id)

		return redirect('/view_tickets.html')



@app.route('/view_tickets.html')
@login_required
@admin_permission.require()
def view_tickets():
	
	tickets = []
	tickets = ticket_controller.get_tickets()
	return render_template('view_tickets.html', tickets=tickets)

@app.route('/dashboard.html')
@login_required
def dashboard():
	curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
	return render_template('dashboard.html', name=curr_user_name)
	
@app.route('/log_out')
@login_required
def log_out():
	logout_user()
	return render_template('log_in.html')

if __name__ == '__main__':
    app.run()