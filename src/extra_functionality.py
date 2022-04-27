from flask_mail import Message
from opf import mail


import vonage

from config import Config

#create a new vonage client obj:
vonage_client = vonage.Client(
    key = 'd576fb48',
    secret = 'l28b1nI0Opk2ujtJ',
    signature_secret = 'BYzr4KcMg8TMRAfXgfSTxjHy87lCRp5PbjI3bljdhXDiF5gxgr'
    )





class Extra_functionality():

    def send_email( email_subj, recipient_email, email_body):
        msg = Message(email_subj, sender = 'opf@gmail.com', recipients = [recipient_email] )
        msg.body = email_body
        mail.send(msg)


    def send_sms_message(to_number, message):
        sms = vonage_client.send_message({ 
            "to": to_number,
            "from": "775-440-8695",
            "text": message,
        })

 