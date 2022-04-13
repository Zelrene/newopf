from distutils.ccompiler import gen_lib_options
from operator import ge
from unicodedata import name
from flask import Flask, Blueprint, abort, render_template, request, redirect, flash, session, url_for

from flask_login import login_required, current_user, logout_user


from .auth import admin_permission, student_permission

import plotly.express as px
import plotly.graph_objects as go
import plotly
import pandas as pd
import json

main_bp = Blueprint(
	"main_bp", __name__, 
	static_folder="static", 
	template_folder="templates")

from src import AnnouncementsController, TicketController, UserController, feedbackController, FaqController

ticket_controller = TicketController.TicketController()
user_controller = UserController.UserController()
feedback_controller = feedbackController.FeedbackController()
faq_controller = FaqController.FaqController()
announcements_controller = AnnouncementsController.AnnouncementsController()

@main_bp.route('/')
def index():
	return redirect(url_for('auth_bp.log_in'))

@main_bp.route('/create_tickets.html', methods = ['GET', 'POST'])
@login_required
def create_tickets():
	if request.method == 'GET':
		isAdmin = user_controller.is_user_admin(current_user.net_id)
		curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
		return render_template('create_tickets.html', name=curr_user_name, isAdmin=isAdmin)
	
	if request.method == 'POST':
		title = request.form['Title']
		description = request.form['Description']
		unit = request.form['Unit#']
		additonalNotes = request.form['AdditionalNotes']
		creator_id = current_user.id
		
		#if not title or not description or not location or not building or not unit:
		if not title or not description or not request.form.get('Location') or not request.form.get('Building') or not request.form.get('Severity_level') or not unit:
			flash('Not all required fields are filled. Please fill all required fields before submitting your ticket.')
			return redirect(url_for('main_bp.create_tickets'))

		else:
			location = request.form['Location']
			building = request.form['Building']
			severity_level = request.form['Severity_level']

			ticket_controller.create_ticket(
				title = title,
				description = description, 
				location = location,
				building = building,
				severity_level = severity_level,
				unit = unit,
				additionalNotes = additonalNotes,
				creator_id = creator_id,
				)

			return redirect(url_for('main_bp.view_tickets'))

@main_bp.route('/view_tickets.html', methods = ['GET', 'POST'])
@login_required
def view_tickets():
	tickets = []
	user_role = user_controller.get_role_with_matching_netid(current_user.net_id)

	if user_role == 'Admin':
		tickets = ticket_controller.get_tickets()
	else:
		tickets = ticket_controller.get_all_tickets_with_matching_user_id(current_user.id)

	if request.method == 'GET':
		curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
		isAdmin = user_controller.is_user_admin(current_user.net_id)

		return render_template('view_tickets.html', tickets=tickets, name=curr_user_name, isAdmin=isAdmin)

# Global Variable for View Single Ticket
curr_ticket_id = 0

@main_bp.route('/view_single_ticket.html', defaults = {'ticket_id' : 0}, methods = ['GET', 'POST'])
@main_bp.route('/view_single_ticket.html/<int:ticket_id>',  methods = ['GET', 'POST'])
@login_required
def view_single_ticket(ticket_id):
	
	# Make sure ticket_id is not 0 (aka NULL)
	global curr_ticket_id
	if ticket_id != 0:
		curr_ticket_id = ticket_id
	else:
		ticket_id = curr_ticket_id

	ticket = ticket_controller.get_single_ticket_with_matching_ticket_id(ticket_id)

	if request.method == 'GET':
		curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
		isAdmin = user_controller.is_user_admin(current_user.net_id)
		
		return render_template('view_single_ticket.html', ticket=ticket, name=curr_user_name, isAdmin = isAdmin)
		
	if request.method == 'POST':
		status = request.form['Status']
		appointment_date = request.form['Appointment_date']
		appointment_time = request.form['Appointment_time']
		admin_message = request.form['Admin_message']
		experience_rate = request.form['Experience_Rate']
		satisfied_level = request.form['Satisfied_Level']
		additional_comments = request.form['Additional_Comments']

		if  request.form['submit_btn'] == 'Delete Ticket':
			ticket_controller.delete_ticket(ticket_id = ticket_id)

		if  request.form['submit_btn'] == 'Resubmit Ticket':
			ticket_controller.resubmit_ticket(ticket_id = ticket_id)



		if  request.form['submit_btn'] == 'Submit':

			feedback_controller.create_feedback(
					ticket_id = ticket_id,
					experience_rate = experience_rate,
					satisfied_level = satisfied_level,
					additional_comments = additional_comments
					)
		
		if  request.form['submit_btn'] == 'Save Changes':
				
			if ticket.status != status:
				ticket_controller.update_ticket_status(
					ticket_id = ticket_id, 
					new_status = status)

			if appointment_date and (appointment_date != str(ticket.appointment_date)):
				ticket_controller.update_appointment_date(
					ticket_id = ticket_id, 
					new_date = appointment_date)

			if appointment_time and (appointment_time != str(ticket.appointment_time)):
				ticket_controller.update_appointment_time(
					ticket_id = ticket_id,
					new_time = appointment_time)

			if admin_message and (admin_message != ticket.admin_message):
				ticket_controller.update_ticket_admin_message(
					ticket_id = ticket_id,
					new_admin_message = admin_message)
			

		return redirect(url_for('main_bp.view_tickets'))


@main_bp.route('/feedback.html',  methods = ['GET'])
@login_required
def feedback():
	#feedback = feedback_controller.get_single_feedback(feedback_id)
	all_feedback = feedback_controller.get_all_feedback()


	if request.method == 'GET':
		curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
		isAdmin = user_controller.is_user_admin(current_user.net_id)
		
		return render_template('feedback.html', name=curr_user_name, isAdmin = isAdmin, all_feedback=all_feedback)
	

@main_bp.route('/dashboard.html', methods = ['GET', 'POST'])
@login_required
def dashboard():
	isAdmin = user_controller.is_user_admin(current_user.net_id)
	curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)

	# get the most recently submitted ticket date
	recent_submission_date = ticket_controller.get_recent_ticket_submission_date()
	
	# get the most recently submiited announcements datetime
	recent_announce_submit_dateTime = announcements_controller.get_recent_announcement_submission_dateTime()

	curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
	isAdmin = user_controller.is_user_admin(current_user.net_id)
			

	if request.method == 'GET':

		if recent_submission_date and recent_announce_submit_dateTime:
			ticket = ticket_controller.get_ticket_with_matching_submitted_date(recent_submission_date)
			recent_announcement = announcements_controller.get_announcement_with_matching_submitted_date(
				submission_dateTime = recent_announce_submit_dateTime)



			return render_template('dashboard.html', ticket = ticket, recent_announcement = recent_announcement, name=curr_user_name, isAdmin=isAdmin, display=True)

	
	if request.method == 'POST':
		announce_title = request.form['Announce_Title']
		announce_descrip = request.form['Announce_Descrip']

		announcements_controller.create_announcement(
			announce_title = announce_title,
			announce_descrip = announce_descrip
		)

		if recent_submission_date and recent_announce_submit_dateTime:
			ticket = ticket_controller.get_ticket_with_matching_submitted_date(recent_submission_date)
			recent_announcement = announcements_controller.get_announcement_with_matching_submitted_date(submission_dateTime = recent_announce_submit_dateTime)

			return render_template('dashboard.html', ticket = ticket, name=curr_user_name, isAdmin=isAdmin, recent_announcement = recent_announcement, display = True)
	
	
	return render_template('dashboard.html', name=curr_user_name, isAdmin=isAdmin, display=False)

@main_bp.route('/faq.html',  methods = ['GET', 'POST'])
@login_required
def faq():
	isAdmin = user_controller.is_user_admin(current_user.net_id)
	curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)

	all_faq = []
	'''
	all_faq = [
		{"question": "who are we?",
		"answer": "we are OPF."},
		{"question": "how to contact us?",
		"answer": "thorugh email."},
		{"question": "can we resubmit a ticket",
		"answer": "yes you will be able to do that."},
		{"question": "How long will it take?",
		"answer": "we do not know at the moment."},
	]
	'''
	all_faq = faq_controller.get_all_faq()

	if request.method == 'GET':
		curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)
		isAdmin = user_controller.is_user_admin(current_user.net_id)
		
		return render_template('faq.html', all_faq = all_faq, name=curr_user_name, isAdmin = isAdmin)
		
	if request.method == 'POST':

		faq_question = request.form['faq_question']
		faq_answer = request.form['faq_answer']

		if  request.form['submit_btn'] == 'Submit':
			faq_controller.create_faq(
				question = faq_question,
				answer = faq_answer
			)


	return render_template('faq.html', all_faq = all_faq, name=curr_user_name, isAdmin=isAdmin)

	
@main_bp.route('/log_out')
@login_required
def log_out():
	logout_user()
	return redirect(url_for('auth_bp.log_in'))

@main_bp.route('/analytics.html')
@login_required
def analytics():
	if current_user.user_role != 'Admin':
		abort(401)

	with admin_permission.require():
		isAdmin = user_controller.is_user_admin(current_user.net_id)
		curr_user_name= user_controller.get_firstLast_name_with_matching_netid(current_user.net_id)

		dorms = ['Argenta Hall', 
				'Canada Hall',
				'Great Basin Hall',
				'Juniper Hall',
				'Living Learning Community',
				'Manzanita Hall',
				'Nye Hall',
				'Peavine Hall',
				'Sierra Hall']
		total_tickets = ticket_controller.get_number_of_tickets_with_matching_buildings(dorms=dorms)

		df_1 = pd.DataFrame({
			"Dorms": dorms,
			"Ticket Count": total_tickets
		})

		fig1 = px.bar(df_1, x="Dorms", y="Ticket Count", 
						title="All Tickets per Residence Halls")
		
		

		table1 = go.Figure(data=[go.Table(
			header = dict(values = [['Dorms'],['# of Tickets']],
				fill_color = 'paleturquoise',
				align=['center', 'center']
			),
			cells = dict(
				values = [dorms, total_tickets],
				align = ['center', 'center']
			)
		)])
		

		genders = ['Female',
					'Male',
					'Did Not Disclose']
		
		genders_to_send = ['F',
						'M',
						'NA']
		residents = user_controller.get_resident_num_with_matching_genders(genders=genders_to_send)
		
		df_2 = pd.DataFrame({
			"Genders": genders,
			"Residents": residents
		})
		
		fig2 = px.pie(df_2, values=residents, names=genders, hole=0.5, title="Genders in Residence Halls")
		
		
		table2 = go.Figure(data=[go.Table(
			header = dict(values = [['Gender'],['# of Residents']],
				fill_color = 'paleturquoise',
				align=['center', 'center']
			),
			cells = dict(
				values = [genders, residents],
				align = ['center', 'center']
			)
		)])
		'''
		width = 600
		height = 400

		# Update Chart sizes
		fig1.update_layout(
			width=width,
			height=height,
			margin=dict(t=60, b=40)
		)
		table1.update_layout(
			width=width,
			height=height,
			margin=dict(t=60, b=40)
		)
		fig2.update_layout(
			width=width,
			height=height,
			margin=dict(t=60, b=40),
			legend=dict(
				orientation="h",
				yanchor="bottom",
				xanchor="right"
			)
		)
		table2.update_layout(
			width=width,
			height=height,
			margin=dict(t=60, b=40)
		)
		'''
		# Make charts to individual JSON objects
		graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
		table1JSON = json.dumps(table1, cls=plotly.utils.PlotlyJSONEncoder)
		graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
		table2JSON = json.dumps(table2, cls=plotly.utils.PlotlyJSONEncoder)
		
		return render_template('analytics.html', 
								name=curr_user_name,
								graph1JSON=graph1JSON, 
								table1JSON=table1JSON, 
								graph2JSON=graph2JSON, 
								table2JSON=table2JSON, 
								isAdmin=isAdmin)
