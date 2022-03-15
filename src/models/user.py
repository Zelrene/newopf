from flask_login import UserMixin
from view import db


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150), nullable = False)
    last_name = db.Column(db.String(150), nullable = False)
    isStudent = db.Column(db.Boolean, nullable = False)
    contact_email = db.Column(db.String(120), nullable = False, unique = True)
    net_id = db.Column(db.String(50), nullable = False, unique = True)
    gender = db.Column(db.Enum('M', 'F', 'NA'), nullable = False)
    student_year = db.Column(db.String(50))
    password = db.Column(db.String(500), nullable = False)


    tickets = db.relationship('Ticket', backref= 'user', lazy = True)
    # a user can have multiple tickets (one to many relationstip)


    def __init__(self, first_name, last_name, isStudent, contact_email, net_id, gender, student_year, password):
        self.first_name = first_name
        self.last_name = last_name
        self.isStudent = isStudent
        self.contact_email = contact_email
        self.net_id = net_id
        self.gender = gender
        self.student_year = student_year
        self.password = password