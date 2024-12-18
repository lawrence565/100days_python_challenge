import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
yc_web_page = res.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_list = soup.select(".titleline>a")
article_text = []
article_link = []
article_upvote = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]
for article in article_list:
    text = article.getText()
    article_text.append(text)
    link = article.get("href")
    article_link.append(link)
print(article_text, article_link, article_upvote)

max_score = max(article_upvote)
index = article_upvote.index(max_score)
print(article_text[index], article_link[index], max_score)

