##################### Extra Hard Starting Project ######################
import pandas, datetime, random, smtplib, os, dotenv

dotenv.load_dotenv()

MY_EMAIL = os.getenv("GMAIL_EMAIL")
PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

# 1. Update the birthdays.csv
try:
    with open("./birthdays.csv") as birthday_file:
        birthday_data = pandas.read_csv(birthday_file)
except FileNotFoundError:
    print("There's no such file or data.")

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.datetime.now()
today_tuple = (today.month, today.day)

birthday_dict = {(row.month, row.day):row for (index, row) in birthday_data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    try:
        with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as birthday_letter:
            content = birthday_letter.read()
            new_content = content.replace("[NAME]", birthday_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=MY_EMAIL, password=PASSWORD)
            conn.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person.email,
                msg=f"Subject:Happy Birthday for you\n\n{new_content}")

    except FileNotFoundError:
        print("There's no such mail template.")

    except Exception as error:
        print(f"There are some problems with SMTP server, {error}")







