from view import db
from src.models.ticket import Ticket
from src.models.user import Role, User

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


    def insert_user(self, first_name, last_name, isStudent, contact_email, net_id, gender, student_year, password):
        new_user = User(
            first_name = first_name,
            last_name = last_name,
            contact_email = contact_email,
            net_id = net_id,
            gender = gender,
            student_year = student_year,
            password = password,
            )
        #new_user.roles.append(Role(name=isStudent))
        role = Role(name = isStudent)
        new_user.roles = [role,]
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

