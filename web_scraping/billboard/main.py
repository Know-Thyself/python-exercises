from bs4 import BeautifulSoup
import requests
import json
import csv

date = input("Which day do you want to travel back in time? Please use this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}").text
soup = BeautifulSoup(response, "html.parser")
titles = soup.select(".o-chart-results-list__item #title-of-a-story")
artists = soup.select(".o-chart-results-list__item #title-of-a-story ~ .c-label")

songs = []

# Extracting and writing text file
text = open("billboard.txt", "w")
for i in range(len(titles)):
    rank_and_song = {"rank": i + 1, "song": titles[i].text.strip(), "artist": artists[i].text.strip()}
    songs.append(rank_and_song)
    text.write(f"{rank_and_song['rank']}. {rank_and_song['song']}\n")

# Writing json file
jsonify = json.dumps(songs, indent=4)
with open("billboard.json", "w") as json_file:
    json_file.write(jsonify)

# Writing csv file
field_names = list(songs[0].keys())
with open('billboard.csv', 'w', encoding='UTF8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(songs)
