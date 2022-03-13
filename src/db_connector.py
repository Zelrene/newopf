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


    def insert_user(self, first_name, last_name, isStudent, contact_email, net_id, nshe_id, gender, year, password):
        new_user = User(
            first_name = first_name,
            last_name = last_name,
            contact_email = contact_email,
            net_id = net_id,
            nshe_id = nshe_id,
            gender = gender,
            year = year,
            password = password,
            isStudent = isStudent)
        db.session.add(new_user)
        db.session.commit()
