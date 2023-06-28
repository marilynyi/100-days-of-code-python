from twilio.rest import Client
from config import config

TWILIO_NUMBER = config.twilio_number
TWILIO_VERIFIED_NUMBER = config.verified_number
TWILIO_ACCOUNT_SID = config.account_sid
TWILIO_AUTH_TOKEN = config.auth_token

class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details.
    """
    
    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
    def send_sms(self, message):
        message = self.client.messages.create(
            body = message,
            from_ = TWILIO_NUMBER,
            to = TWILIO_VERIFIED_NUMBER
        )
        
        print(message.sid)
    
