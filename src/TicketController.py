from src.db_connector import DB_Connector
#from src.models.ticket import Status

database = DB_Connector()

class TicketController(): 

    def get_tickets(self):
        
        tickets = database.select_all_tickets()
        return tickets

    def create_ticket(self, title, creator_id, status, description, severity_level, building, unit, location, additionalNotes, contact): 

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
            contact = contact)

    def update_status(self, new_status):
        database.update_status(new_status)
'''
    def view_single_ticket(self, status): 

        database.insert_status(status)

    def get_status(self):
        
        status = database.select_status()
        return status
'''

