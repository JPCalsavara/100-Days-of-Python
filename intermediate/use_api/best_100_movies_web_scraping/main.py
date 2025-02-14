import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)

web_archive = response.text

soup = BeautifulSoup(web_archive,"html.parser")

all_movies = soup.find_all(name="h3", class_="title")
movies_title = [movie.getText() for movie in all_movies]
movies = movies_title[::-1]
# print(movies)
with open("movies.txt", mode="w", encoding="utf8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
        # print(movie)