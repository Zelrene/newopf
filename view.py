from flask import Flask, abort, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from src import TicketController
'''
		Once controller is made, add this:
from src import UserController

'''

ticket_controller = TicketController.TicketController()
'''
		Once controller is made, add this: 
user_controller = UserController.UserController()

'''

@app.route('/')
def index():
	return redirect('/create_tickets.html')

@app.route('/log_in.html', methods = ['GET', 'POST'])
def log_in():
	if request.method == 'GET':
		return render_template('log_in.html')

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
		nshe_id = request.form['Nshe_Id']
		gender = request.form['Gender']
		year = request.form['Year']
		password = request.form['Password']

		'''
		Once controller is made, add this: 

		user_controller.sign_up(first_name=first_name,
		last_name=last_name,
		isStudent=isStudent,
		contact_email=contact_email,
		net_id=net_id,
		nshe_id=nshe_id,
		gender=gender,
		year=year,
		password=password)

		'''

		return redirect('/log_in.html')

@app.route('/create_tickets.html', methods = ['GET', 'POST'])
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
def view_tickets():
	
	tickets = []
	'''
	ticket_list = [{"title": "Faucet Leak",
	 "description": "Faucet is broken and leaking water", 
	"location": "Bathroom", 
	"building": "Argenta Hall", 
	"unit": "23A", 
	"contact": "student@nevada.unr.edu", 
	"additionalNotes": "N/A"},
	{"title": "Clogged Drain",
	 "description": "Drain is clogged and sink floods", 
	"location": "Bathroom", 
	"building": "Canada Hall", 
	"unit": "24B", 
	"contact": "student2@nevada.unr.edu", 
	"additionalNotes": "N/A"},
	]
	'''
	tickets = ticket_controller.get_tickets()
	return render_template('view_tickets.html', tickets=tickets)

if __name__ == '__main__':
    app.run()