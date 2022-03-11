from src.db_connector import DB_Connector

database = DB_Connector()

class TicketController(): 

    def get_tickets(self):
        
        tickets = database.select_all_tickets()
        return tickets

    def create_ticket(self, title, creator_id, status, description, severity_level, building, unit, location, additionalNotes, contact): 

        database.insert_ticket(title, creator_id, status, description, severity_level, building, unit, location, additionalNotes, contact)



