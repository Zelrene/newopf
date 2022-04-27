from flask_login import UserMixin
from opf import db

#from sqlalchemy import PrimaryKeyConstraint

'''
# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'))


#Define the User data_model
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150), nullable = False)
    last_name = db.Column(db.String(150), nullable = False)
    contact_email = db.Column(db.String(120), nullable = False, unique = True)
    net_id = db.Column(db.String(50), nullable = False, unique = True)
    gender = db.Column(db.Enum('M', 'F', 'NA'), nullable = False)
    student_year = db.Column(db.String(50))
    password = db.Column(db.String(500), nullable = False)

    # Define the user role relationship to Role via UserRoles
    roles = db.relationship('Role', secondary='user_roles')

    # Define the user ticket relationship to Role via tickets
    # a user can have multiple tickets (one to many relationstip)
    tickets = db.relationship('Ticket', backref= 'user', lazy = True)

    def __init__(self, first_name, last_name, contact_email, net_id, gender, student_year, password):
        self.first_name = first_name
        self.last_name = last_name
        self.contact_email = contact_email
        self.net_id = net_id
        self.gender = gender
        self.student_year = student_year
        self.password = password
    

# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))

    def __init__(self, name):
        self.name = name


'''

#creating a new user and role model

#Define the User data_model
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150), nullable = False)
    last_name = db.Column(db.String(150), nullable = False)
    user_role = db.Column(db.String(50), nullable = False)
    contact_email = db.Column(db.String(120), nullable = False, unique = True)
    net_id = db.Column(db.String(50), nullable = False, unique = True)
    gender = db.Column(db.Enum('M', 'F', 'NA'), nullable = False)
    student_year = db.Column(db.String(50))
    password = db.Column(db.String(500), nullable = False)
    phone_number = db.Column(db.String(50), nullable = False)


    # Define the user ticket relationship to Role via tickets
    # a user can have multiple tickets (one to many relationstip)
    tickets = db.relationship('Ticket', backref ='user', lazy = 'dynamic')

    def __init__(self, first_name, last_name, user_role, contact_email, net_id, gender, student_year, password, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.user_role = user_role
        self.contact_email = contact_email
        self.net_id = net_id
        self.gender = gender
        self.student_year = student_year
        self.password = password
        self.phone_number = phone_number
    

    def get_id(self):
        return self.id

    