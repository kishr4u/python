import requests
from plotly import offline


url =  'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers =  {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
response_dict = r.json()

print(response_dict.keys())

repo_dict=response_dict['items']
repo_names, stars = [], []
for repo in repo_dict:
    repo_names.append( repo['name'])
    stars.append(repo['stargazers_count'])

data = [{
    'type':'bar',
    'x':repo_names,
    'y': stars,
    
}]

my_layout = {
       'title': 'Most-Starred Python Projects on GitHub',
       'xaxis': {'title': 'Repository'},
       'yaxis': {'title': 'Stars'},
   }

fig = {'data': data, 'layout': my_layout}
offline.plot(fig,filename='python_repos.html')
