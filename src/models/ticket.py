from email.policy import default
from opf import db
from src.models.user import User 

class Ticket(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(75), nullable = False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    status = db.Column(db.String(25), nullable = False)
    description = db.Column(db.Text, nullable = False)
    severity_level = db.Column(db.String(50), nullable = False)
    building = db.Column(db.String(25), nullable = False)
    unit = db.Column(db.String(25), nullable = False)
    location = db.Column(db.String(50), nullable = False)
    additionalNotes = db.Column(db.Text, nullable = True)
    submission_date = db.Column(db.Date, nullable = False)
    appointment_date = db.Column(db.Date, nullable = True)
    appointment_time = db.Column(db.Time, nullable = True)
    admin_message = db.Column(db.Text, nullable = False)
    
    def __init__(self, title, creator_id, status, description, severity_level, building, unit, location, additionalNotes, submission_date, appointment_date, appointment_time, admin_message):
        self.title = title
        self.creator_id = creator_id
        self.status = status
        self.description = description
        self.severity_level = severity_level
        self.building = building
        self.unit = unit  
        self.location = location
        self.additionalNotes = additionalNotes
        self.submission_date = submission_date
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time  
        self.admin_message = admin_message

    def get_id(self):
        return self.id
