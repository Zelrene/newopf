from opf import db
from src.models.ticket import Ticket
#from src.models.user import Role, User
from src.models.user import User

class DB_Connector():
    def __init__(self):
        db.create_all()

    '''ticket model functions'''
    def insert_ticket(self, title, creator_id, status, description, severity_level, building, unit, location, additionalNotes, submission_date, appointment_date, appointment_time):
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
            submission_date = submission_date,
            appointment_date = appointment_date,
            appointment_time = appointment_time)
        db.session.add(new_ticket)
        db.session.commit()

    def select_all_tickets(self):
        return Ticket.query.all()

    def select_all_tickets_with_matching_user_id(self, user_id):
        tickets = Ticket.query.filter(creator_id = user_id).all()
        return tickets

    def select_single_ticket_with_matching_user_id(self, user_id):
        ticket = Ticket.query.filter(creator_id = user_id).first()
        return ticket

    def select_single_ticket_with_matching_ticket_id(self, ticket_id):
        ticket = Ticket.query.filter(id = ticket_id).first()
        return ticket

    def select_ticket_status(self, ticket_id):
        ticket = self.select_single_ticket_with_matching_ticket_id(ticket_id)
        status = ticket.status
        return status

    def delete_ticket(self, ticket_id):
        ticket_to_del = Ticket.query.filter(id = ticket_id).first()
        db.session.delete(ticket_to_del)
        db.session.commit()

    def update_ticket_status(self, ticket_id, new_status):
        ticket = Ticket.query.filter(id = ticket_id).first()
        ticket.status = new_status
        db.session.commit()

    def update_ticket_appointment_date(self, ticket_id, new_date):
         ticket = Ticket.query.filter(id = ticket_id).first()
         ticket.appointment_date = new_date
         db.session.commit()       

    def update_ticket_appointment_time(self, ticket_id, new_time):
         ticket = Ticket.query.filter(id = ticket_id).first()
         ticket.appointment_date = new_time
         db.session.commit() 

    '''user model functions'''
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