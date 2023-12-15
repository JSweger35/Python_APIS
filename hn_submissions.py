from operator import itemgetter
<<<<<<< HEAD

import requests
#Make an API call and store the response
=======
import requests

# Make an API Call and store the response
>>>>>>> 119b8c2490b7dcc88c632bf8a6bef8e70179049a
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")