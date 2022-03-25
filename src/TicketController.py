from src.db_connector import DB_Connector

from datetime import datetime
from datetime import date

database = DB_Connector()

class TicketController(): 

    def create_ticket(self, title, creator_id, description, severity_level, building, unit, location, additionalNotes,): 
        status = "Submitted"
        submission_date = date.today()
        #couldn't figure out how ti pass in empty date so, passing in current date and time for appointment now
        appointment_date = date.today()
        appointment_time = datetime.now().time()

        database.insert_ticket(title, creator_id, status, description, severity_level, building, unit, location, additionalNotes, submission_date, appointment_date, appointment_time)


    def get_tickets(self):    
        tickets = database.select_all_tickets()
        return tickets

    def get_all_tickets_mathing_id(self):
        pass

