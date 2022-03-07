from src.models import ticket
from view import db
from models.ticket import Ticket

class DB_Connector():
    def __init__(self):
        db.create_all()

    def select_all_tickets():

        return db.session.query(Ticket).all()
    
