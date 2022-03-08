from sqlalchemy import desc
from src.db_connector import DB_Connector

database = DB_Connector()

class TicketController(): 


    def get_tickets():
        
        tickets = database.select_all_tickets()

    def create_ticket(
    title, 
    status, 
    description, 
    severity_level, 
    building, 
    unit, 
    location, 
    additionalNotes, 
    contact): 

        database.insert_ticket(title, status, description, severity_level, building, unit, location, additionalNotes, contact)



