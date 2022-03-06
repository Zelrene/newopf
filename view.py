from turtle import title
from markupsafe import escape
from flask import Flask, abort, render_template, request, redirect
from src import controller
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/create_tickets.html', methods = ['GET', 'POST'])
def create_tickets():
	if request.method == 'GET':
		return render_template('create_tickets.html')
	
	if request.method == 'POST':
		Title = request.form['Title']
		Description = request.form['Description']
		Location = request.form['Location']
		Building = request.form['Building']
		Unit = request.form['Unit#']
		Contact = request.form['Contact']
		AdditonalNotes = request.form['AdditionalNotes']

		return redirect('/')



@app.route('/view_tickets.html')
def view_tickets():
	return render_template('view_tickets.html', tickets = tickets)
