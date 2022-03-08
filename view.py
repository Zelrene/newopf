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
		
		ticket_controller.create_ticket()

		return redirect('/view_tickets.html')



@app.route('/view_tickets.html')
def view_tickets():
	tickets = []
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
	return render_template('view_tickets.html', tickets=ticket_list)


if __name__ == '__main__':
    app.run()