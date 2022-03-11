from flask import Flask, abort, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from src import TicketController

ticket_controller = TicketController.TicketController()

@app.route('/')
def index():
	return redirect('/create_tickets.html')

@app.route('/log_in.html', methods = ['GET', 'POST'])
def log_in():
	if request.method == 'GET':
		return render_template('log_in.html')

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
		creator_id = "Student John"
		
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