import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []
# Explore the first repository
# repo_dict = repo_dicts[0]
# print(f"\nSelected information about each repository:")
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])


# Process results.
print(response_dict.keys())