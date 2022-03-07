
from re import T
from flask import Flask, abort, render_template, request, redirect
from src import controller
from src.models import tickets

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello, World!</h1>'

@app.route('/create_tickets.html', methods = ['GET', 'POST'])
def create_tickets():
	if request.method == 'GET':
		return render_template('create_tickets.html')
	
	if request.method == 'POST':
		title = request.form['Title']
		description = request.form['Description']
		location = request.form['Location']
		building = request.form['Building']
		unit = request.form['Unit#']
		contact = request.form['Contact']
		additonalNotes = request.form['AdditionalNotes']
		return redirect('view_tickets.html')



@app.route('/view_tickets.html')
def view_tickets():
	ticket_list = [tickets.tickets(title="Faucet Leak", 
	description="Water leaking", 
	location="Bathroom", 
	building="Argenta Hall", 
	unit="23A", 
	contact="student1@nevada.unr.edu", 
	additionalNotes="N/A"),
	]

	return render_template('view_tickets.html', tickets=ticket_list)



if __name__ == '__main__':
    app.run()
