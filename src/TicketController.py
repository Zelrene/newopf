from src.db_connector import DB_Connector
from src.models.ticket import Status

database = DB_Connector()

class TicketController(): 

    def get_tickets(self):
        
        tickets = database.select_all_tickets()
        return tickets

    def get_status(self):
        
        status = database.select_status()
        return status

    def create_ticket(self, title, creator_id, description, severity_level, building, unit, location, additionalNotes, contact): 

        database.insert_ticket(title, creator_id, description, severity_level, building, unit, location, additionalNotes, contact)

    def view_single_ticket(self, status): 

        database.insert_status(status)



