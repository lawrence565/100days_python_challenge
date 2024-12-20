import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from os import getenv
from dotenv import load_dotenv

load_dotenv()
X_USER = getenv('TWITTER_EMAIL')
X_PASSWORD = getenv('TWITTER_PASSWORD')


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Edge()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        options = webdriver.EdgeOptions()
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

        # 禁用 WebDriver 標識
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        self.driver.get('https://www.speedtest.net/')

        # accept_button = self.driver.find_element(By.ID, value="_evidon-banner-acceptbutton")
        # accept_button.click()

        time.sleep(10)

        go_btn = self.driver.find_element(By.XPATH,
                                          value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_btn.click()
        time.sleep(30)
        self.down = self.driver.find_element(By.XPATH,
                                             value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                           value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get('https://x.com')
        login_btn = self.driver.find_element(By.XPATH,
                                             value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a')
        login_btn.click()
        time.sleep(3)
        email_input = self.driver.find_element(By.XPATH,
                                               value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email_input.send_keys(X_USER)
        time.sleep(2)
        next_step = self.driver.find_element(By.XPATH,
                                             value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        next_step.click()
        time.sleep(2)
        password_input = self.driver.find_element(By.XPATH,
                                                  value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(X_PASSWORD)
        login = self.driver.find_element(By.XPATH,
                                         value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        login.click()
        time.sleep(1)

        text_area = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[1]')
        text_area.click()
        text_area.send_keys("Test a new tweet on me first post")
        post_btn = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post_btn.click()



Bot = InternetSpeedTwitterBot()
Bot.tweet_at_provider()
