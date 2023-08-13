import requests
from bs4 import BeautifulSoup

URL = "https://editorial.rottentomatoes.com/guide/best-movies-of-2023/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_articles = soup.find_all(name="div", class_="article_movie_title")
list_movies = []
for article in all_articles:
    name_movies = article.find_all('a')
    list_movies.extend(name_movies)

for i in list_movies:
    print(i.text)
