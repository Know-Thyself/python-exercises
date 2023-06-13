import requests
import json

response = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean").json()
general_knowledge_q_and_a = response['results']
# print(json.dumps(general_knowledge_q_and_a, indent=2))
