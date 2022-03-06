from flask import Flask, abort, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from src import controller

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db= SQLAlchemy(app)

from src.models import ticket
from src import db_connector as dbc

db_c = dbc.DB_Connector()

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

		return redirect('/')



@app.route('/view_tickets.html')
def view_tickets():
	return render_template('view_tickets.html')


if __name__ == '__main__':
    app.run()
