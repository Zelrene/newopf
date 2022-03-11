from view import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    isStudent = db.Column(db.Boolean, nullable = False)
    contact_email = db.Column(db.String(120), nullable = False)
    net_id = db.Column(db.String(50), nullable = False)
    nshe_id = db.Column(db.String(50))
    gender = db.Column(db.Enum('M', 'F'), nullable = False)
    year = db.Column(db.Integer)
    password = db.Column(db.String(50), nullable = False)


    ticketcreator = db.relationship('Ticket', backref= 'user', lazy = True)
    #will need experiment more with relationship


    def __init__(self, first_name, last_name, isStudent, contact_email, net_id, nshe_id, gender, year, password):
        self.first_name = first_name
        self.last_name = last_name
        self.isStudent = isStudent
        self.contact_email = contact_email
        self.net_id = net_id
        self.nshe_id = nshe_id
        self.gender = gender
        self.year = year
        self.password = password