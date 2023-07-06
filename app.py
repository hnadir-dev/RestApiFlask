from flask import Flask
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

        params = {
                'q': 'created:2023-06-01..2023-06-01',
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
                return response.json()['items']
        
        return 'requests.get(base_url, headers=headers, params=params)'


asgi_app = WsgiToAsgi(app)