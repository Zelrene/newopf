from src.models.ticket import Ticket
from view import db
from src.models.ticket import Ticket
from src.models.user import User

class DB_Connector():
    def __init__(self):
        db.create_all()

    
    def insert_ticket(self, title, creator_id, status, description, severity_level, building, unit, location, additionalNotes, contact):
        new_ticket = Ticket(
            title = title,
            creator_id = creator_id, 
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

    def select_all_tickets(self):

        return Ticket.query.all()

