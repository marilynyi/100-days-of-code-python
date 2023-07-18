import smtplib
from twilio.rest import Client
from config import config

TWILIO_NUMBER = config.twilio_number
TWILIO_VERIFIED_NUMBER = config.verified_number
TWILIO_ACCOUNT_SID = config.account_sid
TWILIO_AUTH_TOKEN = config.auth_token
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
EMAIL_ADDRESS = config.email_address
EMAIL_PASSWORD = config.email_password

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
    
    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, 587) as connection:
            connection.starttls()
            connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr = EMAIL_ADDRESS,
                    to_addrs = email,
                    msg = f"Subject:New Low Price Flight!\n\n{message}".encode("utf-8")
                )
