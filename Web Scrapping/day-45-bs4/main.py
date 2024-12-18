from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())

all_anchor_tag = soup.findAll(name="a")
# for tag in all_anchor_tag:
#     # print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name='h1', id='name')
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

company_url = soup.select_one(selector="p a")
print(company_url.get("href"))