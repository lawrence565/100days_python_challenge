import smtplib
from os import getenv
from dotenv import load_dotenv

load_dotenv()

EMAIL = getenv('GMAIL_EMAIL')
PASSWORD = getenv('GMAIL_APP_PASSWORD')

def sending_email(name, email, phone, message):

    with smtplib.SMTP('smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(user=EMAIL, password=PASSWORD)
        conn.sendmail(
            from_addr=EMAIL,
            to_addrs=email,
            msg=f"Subject:Received Form Data\n\n" \
                "Here's the data that received through form\n" \
                f"name: {name}\n" \
                f"email: {email}\n" \
                f"phone: {phone}\n" \
                f"message: {message}"
        )
