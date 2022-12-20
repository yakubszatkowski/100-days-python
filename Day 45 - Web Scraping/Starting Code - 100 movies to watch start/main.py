import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
movies_website = response.text
soup = BeautifulSoup(movies_website, 'html.parser')

movie_titles = soup.find_all(name='h3', class_='title')

for movie_title in movie_titles[::-1]:
    print(movie_title.getText())
    with open('movies.txt', mode='a', encoding="utf-8") as file:
        file.write(f'{movie_title.getText()}\n')

