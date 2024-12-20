import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from InternetSpeedTwitterBot import InternetSpeedTwitterBot


PROMISED_DOWN = 100
PROMISED_UP = 10
X_DRIVER_PATH = 'https://x.com/'

Bot = InternetSpeedTwitterBot()
# Bot.get_internet_speed()

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)
driver.get(X_DRIVER_PATH)
time.sleep(2)

Bot.tweet_at_provider()

