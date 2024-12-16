import os, dotenv
from twilio.rest import Client

dotenv.load_dotenv()

ACCOUNT_SID = os.getenv("TWILLO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILLO_AUTH_TOKEN")

class NotificationManager:

    def __init__(self):
        self.client = Client(os.getenv('TWILLO_ACCOUNT_SID'), os.getenv("TWILLO_AUTH_TOKEN"))

    def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.
        Parameters:
        message_body (str): The text content of the SMS message to be sent.
        Returns:
        None
        Notes:
        - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
        message = self.client.messages.create(
            from_=os.getenv("TWILIO_VIRTUAL_NUMBER"),
            body=message_body,
            to=os.getenv("PRIVATE_NUMBER")
        )
        # Prints if successfully sent.
        print(message.sid)