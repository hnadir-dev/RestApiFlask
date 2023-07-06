import json
from flask import Flask
import time
import requests
from asgiref.wsgi import WsgiToAsgi


app = Flask(__name__)

@app.route('/')
def index():
        access_token = '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'
        headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/vnd.github.v3+json'
        }

        base_url = 'https://api.github.com/search/repositories'
        all_repos_names = []

        query = f'created:2023-06-01..2023-06-01'
        while page_number <= 1:
                # Set the request parameters for the current page
                params = {
                'q': query,
                'sort': 'stars',
                'order': 'desc',
                'per_page': 5,
                'page': 1
                }
                # Send the API request
                response = requests.get(base_url, headers=headers, params=params)
                # Check if the request was successful
                if response.status_code == 200:
                        # Get the repositories from the response
                        repositories = response.json()['items']
                        # Add the repositories to the list
                        all_repos_names.extend([{
                                'full_name':repo['full_name'],
                                'url':repo['html_url'],
                                'clone_url':repo['clone_url'],
                                'watchers_count':repo['watchers_count'],
                                'stargazers_count':repo['stargazers_count'],
                                'language':repo['language'],
                                'forks':repo['forks'],
                                'description':repo['description'],
                                'type':repo['owner']['type'],
                                'license':repo['license'],
                                'fork':repo['fork'],
                                'created_at':repo['created_at'],
                                'updated_at':repo['updated_at'],
                                'pushed_at':repo['pushed_at'],
                                } for repo in repositories])
                        # Check if there are more pages to fetch
                        if len(repositories) < per_page:
                                break
                        # Increment the page number for the next request
                        page_number += 1
                else:
                        # Handle the case when the request fails
                        print('API request failed:', response.status_code)
                        break
                time.sleep(1)
        time.sleep(1)
        return json.dump(all_repos_names)

asgi_app = WsgiToAsgi(app)