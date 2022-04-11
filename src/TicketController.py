#from asyncio.windows_events import NULL
from src.db_connector import DB_Connector
#from src.models.ticket import Status

from src.extra_functionality import Extra_functionality 

from datetime import datetime
from datetime import date

from src.models.ticket import Ticket

database = DB_Connector()

class TicketController(): 

    def create_ticket(self, title, creator_id, description, severity_level, building, unit, location, additionalNotes): 
        
        status = "Submitted"
        admin_message = "NA"
        submission_date = date.today()
        appointment_date = None
        appointment_time = None

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
            appointment_time= appointment_time,
            admin_message = admin_message,
            
            )

    ''' 
    def create_admin_message(self, admin_message):
        database.insert_admin_message(
        admin_message = admin_message
        )
    '''
        
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

    def get_admin_message(self, ticket_id):
        admin_message = database.select_admin_message(ticket_id)
        return admin_message
        
    def delete_ticket(self, ticket_id):
        database.delete_ticket(ticket_id)

    def update_ticket_status(self, ticket_id, new_status):
        database.update_ticket_status(ticket_id = ticket_id, new_status = new_status)

        #send email 
        email_subj = "Ticket status update"
        recipeint_email = database.select_creator_email_with_matching_ticket_id(ticket_id)
        recipeint_name = database.select_creator_name_with_matching_ticket_id(ticket_id)
        email_body = "Hi " + recipeint_name + ", \nThe status of your ticket with ticket id " + str(ticket_id) + " has been updated. The new status is " + new_status + ' .'
        Extra_functionality.send_email(
            email_subj = email_subj,
            recipient_email=recipeint_email,
            email_body = email_body
            )

    
    def update_appointment_date(self, ticket_id, new_date):
        database.update_ticket_appointment_date(ticket_id = ticket_id, new_date = new_date)

       #send email 
        email_subj = "Ticket appointment day update"
        recipeint_email = database.select_creator_email_with_matching_ticket_id(ticket_id)
        recipeint_name = database.select_creator_name_with_matching_ticket_id(ticket_id)
        email_body = "Hi " + recipeint_name + ", \nThe appointment day of your ticket with ticket id " + str(ticket_id) + " has been set. Your apppointment is on " + new_date + ' . A facilites member will come to assist with the maintenace issue. we look forward to see you. \nHave a good day.'
        Extra_functionality.send_email(
            email_subj = email_subj,
            recipient_email=recipeint_email,
            email_body = email_body
            )
    
    def update_appointment_time(self, ticket_id, new_time):
        database.update_ticket_appointment_time(ticket_id = ticket_id, new_time = new_time)

    def update_ticket_admin_message(self, ticket_id, new_admin_message):
        database.update_ticket_admin_message(ticket_id = ticket_id, new_admin_message = new_admin_message)

    def get_number_of_tickets_with_matching_single_building(self, dorm):
        tickets_num = database.get_tickets_num_with_matching_single_building(dorm = dorm)
        return tickets_num

  
    def get_number_of_tickets_with_matching_buildings(self, dorms):
        dorms = dorms
        total_tickets = []
        
        for dorm in dorms:
            ticket_num = self.get_number_of_tickets_with_matching_single_building(dorm)
            total_tickets.append(ticket_num)
            
        return total_tickets

    def get_ticket_submission_dates_list( self):
        submission_dates_list = database.select_ticket_submission_dates()

    def get_recent_ticket_submission_date(self):
        tickets = database.select_all_tickets()
        submission_dates_list = []

        for ticket in tickets:
            submission_dates_list.append(ticket.submission_date)
        
        today = date.today()
        recent_submission_date = max(dt for dt in submission_dates_list if dt < today)

        return recent_submission_date

    def get_ticket_with_matching_submitted_date(self, submission_date):
        ticket = database.select_ticket_with_matching_submission_date(submission_date = submission_date)
        return ticket


  

 