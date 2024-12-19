import json, smtplib
from dotenv import load_dotenv
from os import getenv

load_dotenv()

GMAIL_EMAIL = getenv("GMAIL_EMAIL")
GMAIL_APP_PASSWORD = getenv("GMAIL_APP_PASSWORD")

import requests
from bs4 import BeautifulSoup

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-TW,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

res = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1", headers=header)
res.raise_for_status()
print(res.text)
soup = BeautifulSoup(res.text, "html.parser")
price = soup.find(name="span", class_="a-offscreen").get_text()

try:
    with open("base_price.txt") as file:
        content = file.read()
        base_price = json.loads(content)["base_price"]
except FileNotFoundError:
    base_price = int(input(f"The price of the product is {price}, how much would you buy it: "))
    with open("base_price.txt", mode="w") as file:
        json.dump({"base_price": base_price}, file) #ignore type

if price[:2] == "US":
    if float(price[3:]) < float(base_price):
        # with smtplib.SMTP("smtp.gmail.com") as conn:
        #     conn.starttls()
        #     conn.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
        #     conn.sendmail(
        #         from_addr=GMAIL_EMAIL,
        #         to_addrs="5655566haha@gmail.com",
        #         msg = f"Subject:Price Notification\n\nThe product price is now {price}! Go buy it!!!"
        #     )
        print("It's now cheaper.")
else:
    if float(price[1:]) < float(base_price):
        # with smtplib.SMTP("smtp.gmail.com") as conn:
        #     conn.starttls()
        #     conn.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
        #     conn.sendmail(
        #         from_addr=GMAIL_EMAIL,
        #         to_addrs="5655566haha@gmail.com",
        #         msg = f"Subject:Price Notification\n\nThe product price is now {price}! Go buy it!!!"
        #     )
        print("It's now cheaper.")