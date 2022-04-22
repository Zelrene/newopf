from opf import db
from datetime import datetime
from datetime import date

from src.models.ticket import Ticket
#from src.models.ticket import Status
#from src.models.user import Role, User
from src.models.user import User
from src.models.faq import Faq
from src.models.feedback import Feedback
from src.models.announcements import Announcements

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

    def select_ticket_submission_dates(self):
        tickets = Ticket.query.all()
        submission_dates_list = []
        for ticket in tickets:
            submission_dates_list.append(ticket.submission_date)
        
        return submission_dates_list
    
    def select_ticket_with_matching_submission_date(self, submission_date):
        ticket = Ticket.query.filter_by(submission_date = submission_date).first()
        return ticket


    def delete_ticket(self, ticket_id):
        ticket_to_del = Ticket.query.filter_by(id = ticket_id).first()
        feedback_to_del = Feedback.query.filter_by(ticket_id = ticket_id).first()
        if (feedback_to_del):
            db.session.delete(feedback_to_del)
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
        new_time = datetime.strptime(new_time, '%H:%M').time()
        ticket.appointment_time = new_time
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

    def get_tickets_num_with_matching_status(self, status):
        tickets_num = Ticket.query.filter_by(status = status).count()
        
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

    '''announcements model functions'''

    def insert_announcements(self, announce_title, announce_descrip, submission_dateTime):
        
        new_announcements = Announcements(
            announce_title = announce_title,
            announce_descrip = announce_descrip,
            submission_dateTime = submission_dateTime
            )
        
        db.session.add(new_announcements)
        db.session.commit()

    def select_announcements(self):
        all_announcements = Announcements.query.all()
        return all_announcements

    def delete_announcement(self, announcement_id):
        announcement_to_del = Announcements.query.filter_by(id = announcement_id).first()
        db.session.delete(announcement_to_del)
        db.session.commit()

    def update_announce_title(self, announcement_id, new_title):
        announcement = Announcements.query.filter_by(id = announcement_id).first()
        announcement.announce_title = new_title
        db.session.commit()

    def update_announce_descrip(self, announcement_id, new_descrip):
        announcement = Announcements.query.filter_by(id = announcement_id).first()
        announcement.announce_descrip = new_descrip
        db.session.commit()
    
    def update_announce_info(self, announcement_id, new_title, new_descrip):
        announcement = Announcements.query.filter_by(id = announcement_id).first()
        announcement.announce_title = new_title
        announcement.announce_descrip = new_descrip
        db.session.commit()


    def select_announcement_with_matching_submission_dateTime(self, submission_dateTime):
        announcement = Announcements.query.filter_by(submission_dateTime = submission_dateTime).first()
        return announcement

    '''feedback model functions'''
    def insert_feedback(self, ticket_id, experience_rate, satisfied_level, additional_comments, is_completed):
        new_feedback = Feedback(
            ticket_id = ticket_id,
            experience_rate = experience_rate,
            satisfied_level = satisfied_level,
            additional_comments = additional_comments,
            is_completed = is_completed
        )

        db.session.add(new_feedback)
        db.session.commit()

    def update_feedback(self, ticket_id, experience_rate, satisfied_level, additional_comments, is_completed):
        feedback = Feedback.query.filter_by(id = ticket_id).first()
        feedback.experience_rate = experience_rate
        feedback.satisfied_level = satisfied_level
        feedback.additional_comments = additional_comments
        feedback.is_completed = is_completed

        db.session.commit()

    def select_all_feedback(self):
        all_feedback = Feedback.query.all()
        return all_feedback

    def select_all_completed_feedback(self):
        completed_feedback = Feedback.query.filter_by(is_completed = True).all()
        return completed_feedback

    def select_single_feedback(self, feedback_id):
        feedback = Feedback.query.filter_by(id = feedback_id).first()
        return feedback

    def delete_feedback(self, feedback_id):
        feedback_to_del = Feedback.query.filter_by(id = feedback_id).first()
        db.session.delete(feedback_to_del)
        db.session.commit()  
    