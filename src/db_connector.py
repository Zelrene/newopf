from src.models import ticket
from view import db

class DB_Connector():
    def __init__(self):
        db.create_all()

    