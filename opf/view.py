from unicodedata import name
from flask import Flask, Blueprint, abort, render_template, request, redirect, flash, session, url_for

from flask_login import login_required, current_user, logout_user

from .auth import admin_permission, student_permission

main_bp = Blueprint(
	"main_bp", __name__, 
	static_folder="static", 
	template_folder="templates")

from src import TicketController, UserController

ticket_controller = TicketController.TicketController()
user_controller = UserController.UserController()

@main_bp.route('/')
def index():
	return redirect(url_for('auth_bp.log_in'))

@main_bp.route('/create_tickets.html', methods = ['GET', 'POST'])
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
		additonalNotes = request.form['AdditionalNotes']
		status = "Submitted"
		creator_id = current_user.id
		
		if not title or not description or not location or not building or not unit:
			flash('Not all required fields are filled. Please fill all required fields before submitting your ticket.')
			return redirect(url_for('main_bp.create_tickets'))

		ticket_controller.create_ticket(
			title = title,
			description = description, 
			location = location,
			building = building,
			severity_level = severity_level,
			unit = unit,
			additionalNotes = additonalNotes,
			creator_id = creator_id)

		role = user_controller.get_role_with_matching_netid(current_user.net_id)

		'''if role == 'Admin':
			return redirect(url_for('main_bp.view_tickets_admin'))
		else:
		'''
		return redirect(url_for('main_bp.view_tickets'))

@main_bp.route('/view_tickets.html', methods = ['GET', 'POST'])
@login_required
def view_tickets():
	tickets = []
	tickets = ticket_controller.get_tickets()

	if request.method == 'GET':
		#tickets = []
		#status = []
		#status = ticket_controller.get_status()
		#tickets = ticket_controller.get_tickets()
		curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)

		return render_template('view_tickets.html', tickets=tickets, name=curr_user_name)#, status=status)

	if request.method == 'POST':
		for curr_ticket in tickets:
			#print('[[[[[' + curr_ticket.title)
			if request.form['ticket_title'] == curr_ticket.title:
				redirect(url_for('main_bp.view_single_ticket(curr_tickeet)'))



@main_bp.route('/view_single_ticket.html',  methods = ['GET', 'POST'])
@login_required
def view_single_ticket(ticket):
	if request.method == 'GET':
		#tickets = []
		#status = []
		#status = ticket_controller.get_status()
		#tickets = ticket_controller.get_tickets()
		curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
		#return render_template('view_single_ticket.html', tickets=tickets, name=curr_user_name)#, status=status)
		return render_template('viw_single_ticket.html', ticket=ticket, name=curr_user_name)
	
	if request.method == 'POST':
		status = request.form['Status']

		#ticket_controller.view_single_ticket(status = status)
		ticket_controller.update_status(new_status = status)

		role = user_controller.get_role_with_matching_netid(current_user.net_id)

		return redirect(url_for('main_bp.view_single_ticket'))

@main_bp.route('/dashboard.html')
@login_required
def dashboard():
	curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
	return render_template('dashboard.html', name=curr_user_name)

@main_bp.route('/faq.html')
@login_required
def faq():
	curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
	return render_template('faq.html', name=curr_user_name)

	
@main_bp.route('/log_out')
@login_required
def log_out():
	logout_user()
	return redirect(url_for('auth_bp.log_in'))

@main_bp.errorhandler(403)
@login_required
def page_not_found(e):
	session['redirected_from'] = request.url
	curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
	title = 'Sorry, Page Not Found'
	message = 'The page you requested does not exist. You may have followed a bad link, or the page may have been moved or removed.'
	return render_template('page_not_found.html', name=curr_user_name, title=title, message=message, show=True)

@main_bp.errorhandler(401)
def page_not_found(e):
	session['redirected_from'] = request.url
	title = 'Unauthorized Page'
	message = 'The page you are trying to access is unavailable. You lack the valid authentication credentials to view this page.'
	return render_template('page_not_found.html', title=title, message=message, show=False)

@main_bp.errorhandler(400)
def page_not_found(e):
	session['redirected_from'] = request.url
	title = 'Bad Directory'
	message = 'The page you are trying to access is unavailable. The page that directed you here should not have made a link to this page.'
	return render_template('page_not_found.html', title=title, message=message, show=True)