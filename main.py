# from bs4 import BeautifulSoup
# import requests

import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

# URL = "https://www.nytimes.com/article/best-movies-netflix.html"
# response = requests.get(URL)
# movie_data = response.text
#
# soup = BeautifulSoup(movie_data, "html.parser")
# all_title = soup.find_all(name="h2", class_="css-ow6j0y eoo0vm40")
# for title in all_title:
#     head = title.getText()
#     print(head)




# response = requests.get("https://news.ycombinator.com/newest")
# yc_page = response.text
#
# soup = BeautifulSoup(yc_page, "html.parser")
# all_title = soup.find_all(name='a', class_="titlelink")
# for item in all_title:
#     article_text = (item.getText())
#     article_link = (item.get("href"))
#     print((article_text, article_link))









# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchor = soup.find_all(name="a")
# for link in all_anchor:
#     print(link.get("href"))
