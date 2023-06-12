import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit("No argument has been provided!")

band_name = sys.argv[1]
response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=50&term={band_name}").json()

print(json.dumps(response, indent=2))
print(f"List of songs by the {band_name}")
for res in response['results']:
    print(res['trackName'])
