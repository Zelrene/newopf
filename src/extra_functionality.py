from flask_mail import Message
from opf import mail

class Extra_functionality():

    def send_email( email_subj, recipient_email, email_body):
        msg = Message(email_subj, sender = 'opf@gmail.com', recipients = [recipient_email] )
        msg.body = email_body
        mail.send(msg)
