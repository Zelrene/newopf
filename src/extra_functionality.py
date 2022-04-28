from flask_mail import Message
from opf import mail, sms

from config import Config

class Extra_functionality():

    def send_email( email_subj, recipient_email, email_body):
        msg = Message(email_subj, sender = 'opf@gmail.com', recipients = [recipient_email] )
        msg.body = email_body
        mail.send(msg)


    def send_sms_message(to_number, message):
        response = sms.send_message({ 
            "from": '18663481396',
            "to": '17754408695',
            "text": message,
        })
        '''
        if response["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print("Message failed with error: {response['messages'][0]['error-text']}")
        '''
