from multiprocessing import connection
from src.models.ticket import Ticket
from view import db
from src.models.ticket import Ticket

class DB_Connector():
    def __init__(self):
        db.create_all()

    def select_all_tickets():

        return db.session.query(Ticket).all()
    
    def insert_ticket(self, title, status, description, severity_level, building, unit, location, additionalNotes, contact):
        new_ticket = Ticket(
            title = title, 
            status = status, 
            severity_level = severity_level, 
            description = description, 
            building = building, 
            unit = unit, 
            location = location, 
            additionalNotes = additionalNotes, 
            contact = contact)
        db.session.add(new_ticket)
        db.session.commit()


