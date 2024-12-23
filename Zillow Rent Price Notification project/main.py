import requests, re, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

pattern = r"\$\d[\d,]*"

# Fetch the data
res = requests.get('https://appbrewery.github.io/Zillow-Clone/')
soup = BeautifulSoup(res.text, 'html.parser')
address_list = soup.findAll(name='address')
rent_list = soup.findAll(name='div', class_='PropertyCardWrapper')
link_list = soup.findAll(name='a', class_='StyledPropertyCardDataArea-anchor')


# Fetch the form
edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option('detach', value=True)
driver = webdriver.Edge(options=edge_option)
driver.get('https://forms.gle/hSBs4YFYUPuE3gGv6')
time.sleep(1)
address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
submit_btn = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

for i in range(len(address_list)):
    address_input.send_keys(address_list[i].text.strip())
    price = re.search(pattern, rent_list[i].text)
    price_input.send_keys(price.group())
    link_input.send_keys(link_list[i].get('href'))
    submit_btn.click()
    driver.get('https://forms.gle/hSBs4YFYUPuE3gGv6')
    time.sleep(1)















