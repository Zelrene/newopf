from src.models import ticket
from view import db

class DB_Connector():
    def __init__(self):
        db.create_all()

    '''
    def add_ticket(self, id, status, severity_level, description, building, unit, title, location, additionalNotes, contact):
        new_ticket = ticket(id, status, severity_level, description, building, unit, title, location, additionalNotes, contact)
        db.session.add(new_ticket)
        db.session.commit(new_ticket)
    '''
    
