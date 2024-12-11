import smtplib, dotenv, os, datetime, random

dotenv.load_dotenv()

MY_EMAIL = os.getenv("GMAIL_EMAIL")
PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

today = datetime.datetime.now()
if today.weekday() == 2:
    with open("./quotes.txt") as quote_file:
        quote_list = quote_file.readlines()
        quote = random.choice(quote_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Start the connection
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="5655566haha@gmail.com",
            msg=f"Subject:Monday Quotes\n\n{quote}")
