from opf import db
from src.models.ticket import Ticket
from src.models.ticket import Status
#from src.models.user import Role, User
from src.models.user import User

class DB_Connector():
    def __init__(self):
        db.create_all()

    def insert_ticket(self, title, creator_id, description, severity_level, building, unit, location, additionalNotes, contact):
        new_ticket = Ticket(
            title = title,
            creator_id = creator_id, 
            severity_level = severity_level, 
            description = description, 
            building = building, 
            unit = unit, 
            location = location, 
            additionalNotes = additionalNotes, 
            contact = contact)
        db.session.add(new_ticket)
        db.session.commit()

    def insert_status(self, status):
        new_status = Status(
            status = status)
        db.session.add(new_status)
        db.session.commit()

    def select_all_tickets(self):
        return Ticket.query.all()

    def select_status(self):
        return Status.query.all()


    def insert_user(self, first_name, last_name, user_role, contact_email, net_id, gender, student_year, password):
        new_user = User(
            first_name = first_name,
            last_name = last_name,
            user_role = user_role,
            contact_email = contact_email,
            net_id = net_id,
            gender = gender,
            student_year = student_year,
            password = password,
            )


        #role = Role(name = isStudent,)
        #new_user.roles = [role,]

        db.session.add(new_user)
        db.session.commit()
        



    def select_all_user(self):
            return User.query.all()

    def select_user_with_matching_email(self, contact_email):
        user = User.query.filter_by(contact_email = contact_email).first()
        return user

    def select_user_with_matching_netid(self, net_id):
        user = User.query.filter_by(net_id= net_id).first()
        return user

    def select_password_with_matching_email(self, contact_email):
        user = self.select_user_with_matching_email(contact_email)
        return user.password

    def select_password_with_matching_netid(self, net_id):
        user = self.select_user_with_matching_netid(net_id)
        return user.password

    def select_first_name_with_matching_email(self, contact_email):
        user = self.select_user_with_matching_email(contact_email)
        return user.first_name

    def select_first_name_with_matching_netid(self, net_id):
        user = self.select_user_with_matching_netid(net_id)
        return user.first_name

    def select_last_name_with_matching_email(self, contact_email):
        user = self.select_user_with_matching_email(contact_email)
        return user.last_name

    def select_last_name_with_matching_netid(self, net_id):
        user = self.select_user_with_matching_netid(net_id)
        return user.last_name

    def select_role_with_matching_email(self, contact_email):
        user = self.select_user_with_matching_email(contact_email)
        return user.user_role

    def select_role_with_matching_netid(self, net_id):
        user = self.select_user_with_matching_netid(net_id)
        return user.user_role