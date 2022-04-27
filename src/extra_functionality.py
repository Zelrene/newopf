from flask_mail import Message
from opf import mail

'''
#for send notifiation through message
from dotenv import load_dotenv
import vonage
from .util import env_var, extract_error

#load environmental variables from a .env file:
load_dotenv('.env')

#load in config from env variables:
VONAGE_API_KEY = env_var('VONAGE_API_KEY')
VONAGE_API_SECRET = env_var('VONAGE_API_SECRET')
VONAGE_NUMBER = env_var('VONAGE_NUMBER')

#create a new vonage client obj:
vonage_client = vonage.Client(
    api_key = VONAGE_API_KEY,
    api_secret = VONAGE_API_SECRET
    )

'''

class Extra_functionality():

    def send_email( email_subj, recipient_email, email_body):
        msg = Message(email_subj, sender = 'opf@gmail.com', recipients = [recipient_email] )
        msg.body = email_body
        mail.send(msg)
