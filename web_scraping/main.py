from bs4 import BeautifulSoup
import requests
# import lxml

with open("example.html", encoding="utf8") as file:
    soup = BeautifulSoup(file, "html.parser")

response = requests.get("https://news.ycombinator.com/").text
soup = BeautifulSoup(response, "html.parser")
print(soup.prettify())
articles = soup.find_all(class_="titleline")
scores = soup.find_all(class_="score")
print(articles)
titles = []
links = []
for article in articles:
    print(article.text)
    titles.append(article.text)
    print(article.a.get("href"))
    links.append(article.a.get("href"))
points = []
for score in scores:
    print(score)
    print(int(score.text.split()[0]))
    points.append(int(score.text.split()[0]))

idx = points.index(max(points))
print(idx, '<<<<< index')
print(articles[idx])
