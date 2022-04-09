
from opf import db
from src.models.ticket import Ticket


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key = True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable = False, unique = True)
    experience_rate = db.Column(db.Integer, nullable = False)
    satisfied_level = db.Column(db.Enum('Yes', 'No', 'Could improve'), nullable = False)
    additional_comments = db.Column(db.Text, nullable = False)

    
    def __init__(self, ticekt_id, experience_rate, satisfied_level, additional_comments):
        self.ticket_id = ticekt_id
        self.experience_rate = experience_rate
        self.satisfied_level = satisfied_level
        self.additional_comments = additional_comments