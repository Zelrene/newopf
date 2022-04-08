from opf import db
from datetime import datetime
from datetime import date

from src.models.ticket import Ticket
#from src.models.ticket import Status
#from src.models.user import Role, User
from src.models.user import User
from src.models.faq import Faq
from src.models.feedback import Feedback

class DB_Connector():
    def __init__(self):
        db.create_all()

    '''ticket model functions'''

    def insert_ticket(self, title, creator_id, status, description, severity_level, building, unit, location, additionalNotes, submission_date, appointment_date, appointment_time, admin_message):
        
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
            appointment_time = appointment_time,
            admin_message = admin_message)

        db.session.add(new_ticket)
        db.session.commit()

    def select_all_tickets(self):
        tickets = Ticket.query.all()
        return tickets

    '''
    def insert_admin_message(self, admin_message):
        new_admin_message = Ticket(
            admin_message=admin_message
        )
        db.session.add(new_admin_message)
        db.session.commit()
    '''

    def select_all_tickets_with_matching_user_id(self, user_id):
        tickets = Ticket.query.filter_by(creator_id = user_id).all()
        return tickets

    def select_single_ticket_with_matching_user_id(self, user_id):
        ticket = Ticket.query.filter_by(creator_id = user_id).first()
        return ticket

    def select_single_ticket_with_matching_ticket_id(self, ticket_id):
        ticket = Ticket.query.filter_by(id = ticket_id).first()
        return ticket

    def select_ticket_status(self, ticket_id):
        ticket = self.select_single_ticket_with_matching_ticket_id(ticket_id)
        status = ticket.status
        return status

    def select_admin_message(self, ticket_id):
        ticket = self.select_single_ticket_with_matching_ticket_id(ticket_id)
        admin_messsge = ticket.admin_message
        return admin_messsge
        
    def select_creator_email_with_matching_ticket_id(self, ticket_id):
        ticket = Ticket.query.filter_by(id = ticket_id).first()
        creator_email =  ticket.user.contact_email
        return creator_email

    def select_creator_name_with_matching_ticket_id(self, ticket_id):
        ticket = Ticket.query.filter_by(id = ticket_id).first()
        first_name = ticket.user.first_name
        last_name = ticket.user.last_name 
        name = first_name + " " + last_name
        return name

    def delete_ticket(self, ticket_id):
        ticket_to_del = Ticket.query.filter_by(id = ticket_id).first()
        db.session.delete(ticket_to_del)
        db.session.commit()

    def update_ticket_status(self, ticket_id, new_status):
        ticket = Ticket.query.filter_by(id = ticket_id).first()
        ticket.status = new_status
        db.session.commit()

    def update_ticket_appointment_date(self, ticket_id, new_date):
        ticket = Ticket.query.filter_by(id = ticket_id).first()
        new_date = datetime.strptime(new_date, '%Y-%m-%d')
        ticket.appointment_date = new_date
        db.session.commit()       

    def update_ticket_appointment_time(self, ticket_id, new_time):
        ticket = Ticket.query.filter_by(id = ticket_id).first()
        #the format(%H:%M:S) might need to changed depending on what is being sent to the user 
        new_time = datetime.strptime(new_time, '%H:%M:%S')
        ticket.appointment_date = new_time
        db.session.commit() 
    
    def update_ticket_admin_message(self, ticket_id, new_admin_message):
        ticket = Ticket.query.filter_by(id = ticket_id).first()
        ticket.admin_message = new_admin_message
        db.session.commit()

    def get_tickets_num_with_matching_single_building(self, dorm):
        tickets_num = Ticket.query.filter_by(building = dorm).count()
        
        if(tickets_num):
            tickets_num = tickets_num
        else:
            tickets_num = 0
        
        return tickets_num



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
        users = User.query.all()
        return users

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


    def get_residents_num_with_matching_gender(self, gender):
        residents_num = User.query.filter_by(gender = gender).count()
        
        if(residents_num):
            residents_num = residents_num
        else:
            residents_num = 0
        
        return residents_num

    '''faq model functions'''

    def insert_faq(self, question, answer):
        
        new_faq = Faq(
            question = question,
            answer = answer
            )
        
        db.session.add(new_faq)
        db.session.commit()

    def select_all_faq(self):
        all_faq = Faq.query.all()
        return all_faq

    def delete_faq(self, faq_id):
        faq_to_del = Faq.query.filter_by(id = faq_id).first()
        db.session.delete(faq_to_del)
        db.session.commit()


    '''feedback model functions'''
    def insert_feedback(self, ticket_id, experience_rate, satisfied_level, additional_comments):
        new_feedback = Feedback(
            ticekt_id = ticket_id,
            experience_rate = experience_rate,
            satisfied_level = satisfied_level,
            additional_comments = additional_comments
        )

        db.session.add(new_feedback)
        db.session.commit()

    def select_all_feedback(self):
        all_feedback = Feedback.query.all()
        return all_feedback

    def select_single_feedback(self, feedback_id):
        feedback = Feedback.query.filter_by(id = feedback_id).first()
        return feedback

    def delete_feedback(self, feedback_id):
        feedback_to_del = Feedback.query.filter_by(id = feedback_id).first()
        db.session.delete(feedback_to_del)
        db.session.commit()  
    