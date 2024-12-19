import time
from os import getenv
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

linkedin_account = getenv("LINKEDIN_ACCOUNT")
linkedin_password = getenv("LINKEDIN_PASSWORD")

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://www.linkedin.com/feed/")

# Click login problem
# login = driver.find_element(By.XPATH, value="/html/body/nav/div/a[2]")
# login.click()
# time.sleep(1)

# Login LinkedIn
account_input = driver.find_element(By.XPATH, value='//*[@id="username"]')
password_input = driver.find_element(By.XPATH, value='//*[@id="password"]')
account_input.send_keys(linkedin_account)
password_input.send_keys(linkedin_password)

sign_in = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[4]/button')
sign_in.click()
time.sleep(2)

job_tab = driver.find_element(By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')
job_tab.click()
time.sleep(3)

# Setting Job
job_name = driver.find_element(By.CSS_SELECTOR, value='input[aria-label="Search by title, skill, or company"]')
job_name.send_keys("React")
job_name.send_keys(Keys.ENTER)
time.sleep(4)
job_location = driver.find_element(By.CSS_SELECTOR, value='input[aria-label="City, state, or zip code"]')
job_location.click()
job_location.clear()
job_location.send_keys("Taipei, Taipei City, Taiwan")

# Save Job base on the result
job_ul = driver.find_element(By.CSS_SELECTOR, value='//*[@id="main"]/div/div[2]/div[1]/div/ul')
job_list = job_ul.find_elements(By.TAG_NAME, value='li')
for job in job_list:
    job.click()
    save_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[6]/div/button')
    save_button.click()
