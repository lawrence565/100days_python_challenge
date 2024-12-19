from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")
FName = driver.find_element(By.NAME, value="fName")
FName.send_keys("Lawrence")
LName = driver.find_element(By.NAME, value="lName")
LName.send_keys("Wu")
Email = driver.find_element(By.NAME, value="email")
Email.send_keys("lawrence891106@gmail.com")

sign_up = driver.find_element(By.TAG_NAME, value="button")
sign_up.click()