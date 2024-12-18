import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

res = requests.get(url=URL)
soup = BeautifulSoup(res.text, "html.parser")

title_list = soup.findAll(name="h3", class_="title")
title_list = [title.getText() for title in title_list]
title_list = title_list[::-1]

with open("movie.txt", mode="w") as file:
    for title in title_list:
        file.writelines(title + "\n")

