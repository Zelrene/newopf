'''
from view import db_c

class Controller:

    def add_ticket_to_db(title, description, location, building, unit, severity_level, contact, additionalNotes):

        status = "Pending"

        db_c.add_ticket(title, status, description, severity_level, building, unit, location, additionalNotes, contact)


''' 