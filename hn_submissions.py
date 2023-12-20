from operator import itemgetter

import requests

# Make an API Call and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make seperate API calls for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    submission_dict = {
        'title' : response_dict['Title'],
        'hn_link' : f"https://news.ycombinator.com/item?id={submission_id}",
        'comments' : response_dict['comments'],
    }
    submission_dicts.append(submission_dict)