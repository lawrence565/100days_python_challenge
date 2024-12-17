import os, dotenv

from data_manager import DataManager

from twilio.rest import Client
import smtplib

dotenv.load_dotenv()

class NotificationManager:

    def __init__(self):
        self.client = Client(os.getenv('TWILLO_ACCOUNT_SID'), os.getenv("TWILLO_AUTH_TOKEN"))
        self.email_address = os.getenv("GMAIL_EMAIL")
        self.email_password = os.getenv("GMAIL_APP_PASSWORD")

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

    def send_email(self, email, message_body):
        """
        Sends an email message through the SMTPlib module.
        This function takes a message body as input and uses the SMTPlib module to send
        an email from a official email to user's own email address.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.

        Parameters:
        email(str): The email address received the message with.
        message_body (str): The text content of the SMS message to be sent.

        Returns:
        None
        """
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=self.email_address, password=self.email_password)
            conn.sendmail(
                from_addr=self.email_address,
                to_addrs=email,
                msg=f"Subject:New Flight Deals\n\n{message_body}")

# notification_manager = NotificationManager()
# dataManager = DataManager()
# dataManager.get_user_data()
# for user in dataManager.user_data:
#     notification_manager.send_email(
#                     email=user['emailAddress'],
#                     message_body=f"Hi {user['firstName']}, Low price alert! Only NT${10000} to fly "
#                                  f"from TPE to NRT, "
#                                  f"on today until 2025/01/01.")