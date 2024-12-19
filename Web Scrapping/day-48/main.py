from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Edge browser open after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://www.python.org/")
event_list = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul').text.split("\n")
event_dict = {}
for i in range(0, len(event_list), 2):
    event_dict[i] = {
        'time': event_list[i],
        'name': event_list[i + 1]
    }
print(event_dict)

driver.close()  # Close a single tab
driver.quit()  # Shut down the entire browser
