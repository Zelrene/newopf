from multiprocessing import connection
from src.models import ticket
from view import db
from src.models.ticket import Ticket

class DB_Connector():
    def __init__(self):
        db.create_all()

    def select_all_tickets():

        return db.session.query(Ticket).all()
    
    def add_ticket(self, id, status, severity_level, description, building, unit, title, location, additionalNotes, contact):
        new_ticket = ticket(id, status, severity_level, description, building, unit, title, location, additionalNotes, contact)
        db.session.add(new_ticket)
        db.session.commit(new_ticket)


