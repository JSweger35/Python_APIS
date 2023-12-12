import requests
import json

# Make an API call, and store the response
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structuree of the data
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open(readanble_file, 'w') as f:
    json.dump(response_dict, f, indent=4)