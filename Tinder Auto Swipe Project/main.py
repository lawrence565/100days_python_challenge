import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from sphinx.util.console import light

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://tinder.com/")
time.sleep(2)
tinder_window = driver.current_window_handle

cookie_accept = driver.find_element('xpath', '//*[@id="q2098069830"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div')
cookie_accept.click()
time.sleep(1)

login = driver.find_element(By.CSS_SELECTOR, 'a.c1p6lbu0')
login.click()
time.sleep(1)

login_with_facebook = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Log in with Facebook"]')
login_with_facebook.click()
time.sleep(2)

# Change to new pop-up window
for handle in driver.window_handles:
    if handle != tinder_window:
        driver.switch_to.window(handle)
        break

facebook_user = driver.find_element(By.XPATH, '//*[@id="email"]')
facebook_user.send_keys('lawrence891106@gmail.com')
facebook_password = driver.find_element(By.XPATH, '//*[@id="pass"]')
facebook_password.send_keys('Aa634225@Meta')
facebook_login = driver.find_element(By.NAME, 'login')
facebook_login.click()
facebook_continue = driver.find_element(By.XPATH, value='//*[@id="mount_0_0_jF"]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div[1]/div/span/span')
facebook_continue.click()
driver.switch_to.window(tinder_window)
time.sleep(3)

allow_location = driver.find_element(By.CSS_SELECTOR, value='#q369688754 > div > div > div > div > div.Bgc\(\$c-ds-background-primary\).Py\(24px\).Px\(36px\) > button:nth-child(1)')
allow_location.click()
right_slide = driver.find_element(By.CSS_SELECTOR, value='#q2098069830 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > div > div > main > div > div > div > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\).TranslateY\(55\%\) > div > div:nth-child(4) > button')
for i in range(20):
    right_slide.click()

