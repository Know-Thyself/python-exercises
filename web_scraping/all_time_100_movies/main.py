from bs4 import BeautifulSoup
import requests
import json
from movie import Movie

response = requests.get("https://www.timeout.com/film/best-movies-of-all-time").text
soup = BeautifulSoup(response, "html.parser")
titles = soup.find_all(class_="_h3_cuogz_1")
images = soup.find_all(name="img")
summaries = soup.find_all(class_="_summary_kc5qn_21")
images = [
    img.get("src") for img in images[1:] if not img.get("src").startswith("data")
]

movies = []

# Creating a movie instance and list
for i in range(100):
    temp_list = titles[i].text.split()
    title = " ".join(temp_list[1:])
    rank = int(temp_list[0].replace(".", ""))
    image = images[i]
    summary = summaries[i].text
    movie = Movie(i + 1, title, image, rank, summary)
    movies.append(vars(movie))

# Creating a json file
json_object = json.dumps(movies, indent=4)
with open("movies.json", "w") as file:
    file.write(json_object)

# Creating a text file
write_text_file = open("movies.txt", "w")
for movie in movies:
    line = f"{movie['rank']}. {movie['title']}"
    write_text_file.write(f"{line}\n")
