from twilio.rest import Client

TWILIO_SID = "AC55d29c322eef608c27b7c26bcb1be6e8"
TWILIO_AUTH_TOKEN = 'bf7bb5876323747f8fdce999b379e8fe'

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_messages(self, notification):
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=notification,
            from_='+12097216352',
            to='+6289699501548'
        )