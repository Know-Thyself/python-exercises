from bs4 import BeautifulSoup
import requests
import json

response = requests.get("https://www.timeout.com/film/best-movies-of-all-time").text
soup = BeautifulSoup(response, "html.parser")
movies_soup = soup.find_all(class_="_h3_cuogz_1")
images_soup = soup.find_all(name="img")
summaries_soup = soup.find_all(class_="_summary_kc5qn_21")
print(summaries_soup)


titles = []
images = []
summaries = []
list_of_dict = []

for movie in movies_soup:
    titles.append(movie.text)

for image in images_soup:
    image_src = image.get("src")
    if not image_src.startswith("data"):
        images.append(image_src)

for summary in summaries_soup:
    summaries.append(summary.text)

# Generating dictionaries of movies
for i in range(100):
    movies_dict = {}
    temp_list = titles[i].split()
    movies_dict["title"] = " ".join(temp_list[1:])
    movies_dict["image"] = images[1:][i]
    movies_dict["rank"] = int(temp_list[0].replace(".", ""))
    movies_dict["summary"] = summaries[i]
    list_of_dict.append(movies_dict)

json_object = json.dumps(list_of_dict, indent=4)
with open("movies.json", "w") as file:
    file.write(json_object)

# Writing a text file
write_text_file = open("movies.txt", "w")
for movie in list_of_dict:
    line = f"{movie['rank']}. {movie['title']}"
    write_text_file.write(f"{line}\n")