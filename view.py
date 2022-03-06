#from turtle import title
#from markupsafe import escape
from flask import Flask, abort, render_template, request, redirect
from src import controller
from src.models import tickets
from src.templates import layout

app = Flask(__name__)


@app.route('/')
def hello():
		return '<h1>Hello World!</h1>'
		
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

		return redirect('/')



@app.route('/view_tickets.html')
def view_tickets():
	return render_template('view_tickets.html')
