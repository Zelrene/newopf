from src.db_connector import DB_Connector
#from src.models.ticket import Status

from flask_mail import Message
from opf import mail

from datetime import datetime
from datetime import date

database = DB_Connector()

class TicketController(): 

    def create_ticket(self, title, creator_id, description, severity_level, building, unit, location, additionalNotes,): 
        
        status = "Submitted"
        submission_date = date.today()
        #couldn't figure out how to pass in empty date so, passing in current date and time for appointment for now now
        appointment_date = date.today()
        appointment_time = datetime.now().time()

        database.insert_ticket(
            title = title,
            creator_id = creator_id,
            status = status, 
            description = description, 
            severity_level = severity_level, 
            building = building, 
            unit = unit, 
            location = location, 
            additionalNotes = additionalNotes, 
            submission_date = submission_date, 
            appointment_date = appointment_date, 
            appointment_time= appointment_time
            )


    def get_tickets(self):    
        tickets = database.select_all_tickets()
        return tickets

    def get_all_tickets_with_matching_user_id(self, user_id):
        tickets = database.select_all_tickets_with_matching_user_id(user_id)
        return tickets

    def get_single_ticket_with_matching_ticket_id(self, user_id):
        ticket = database.select_single_ticket_with_matching_user_id(user_id)
        return ticket

    def get_single_ticket_with_matching_ticket_id(self, ticket_id):
        ticket = database.select_single_ticket_with_matching_ticket_id(ticket_id)
        return ticket

    def get_ticket_status(self, ticket_id):
        status = database.select_ticket_status(ticket_id)
        return status

    def delete_ticket(self, ticket_id):
        database.delete_ticket(ticket_id)

    def update_ticket_status(self, ticket_id, new_status):
        database.update_ticket_status(ticket_id = ticket_id, new_status = new_status)

        #send email 
        msg = Message('Ticket Status update', sender = 'opf@gmail.com', recipients = ['njuana@nevada.unr.edu'])
        msg.body = "The status of your ticket with ticket id " + str(ticket_id) + " has be updated. The new status is " + new_status + ' .'
        mail.send(msg)
        #print("mail is sent.")

    def update_appointment_date(self, ticket_id, new_date):
        database.update_ticket_appointment_date(ticket_id = ticket_id, new_date = new_date)
    
    def update_appointment_time(self, ticket_id, new_time):
        database.update_ticket_appointment_time(ticket_id = ticket_id, new_time = new_time)