from bs4 import BeautifulSoup
import requests
import json
import csv
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

load_dotenv()

date = input(
    "Which day do you want to travel back in time? Please use this format YYYY-MM-DD: "
)

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}").text
soup = BeautifulSoup(response, "html.parser")
titles = soup.select(".o-chart-results-list__item #title-of-a-story")
artists = soup.select(".o-chart-results-list__item #title-of-a-story ~ .c-label")

songs = []

# Extracting and writing text file
text = open("billboard.txt", "w")
for i in range(len(titles)):
    rank_and_song = {
        "rank": i + 1,
        "song": titles[i].text.strip(),
        "artist": artists[i].text.strip(),
    }
    songs.append(rank_and_song)
    text.write(f"{rank_and_song['rank']}. {rank_and_song['song']}\n")

# Writing json file
jsonify = json.dumps(songs, indent=4)
with open("billboard.json", "w") as json_file:
    json_file.write(jsonify)

# Writing csv file
field_names = list(songs[0].keys())
with open("billboard.csv", "w", encoding="UTF8", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(songs)

# Filling google form with selenium
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("-incognito")
options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=options)
url = os.getenv("GOOGLE_FORM_URL")

for song in songs:
    driver.get(url)
    time.sleep(1)
    rank_input = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
    )

    song_input = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
    )
    artist_input = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
    )
    submit = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
    )
    rank_input.send_keys(song["rank"])
    song_input.send_keys(song["song"])
    artist_input.send_keys(song["artist"])
    submit.click()
    reload_from = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    reload_from.click()
    time.sleep(1)
