import os

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_CSE_ID = os.getenv('GOOGLE_CSE_ID')

import requests

class ResultObj:
    def __init__(self, title, link, description):
        self.title = title
        self.url = link
        self.description = description
    
def search(query, advanced=False, num_results=10):
    url = 'https://www.googleapis.com/customsearch/v1?' \
          f'key={GOOGLE_API_KEY}&' \
          f'cx={GOOGLE_CSE_ID}&' \
          f'num={num_results}&' \
          f'q={query}'
    res = requests.get(url)
    json = res.json()
    res.close()

    for item in json['items']:
        if advanced:
            yield ResultObj(
                item['title'], 
                item['link'], 
                item['snippet'] if 'snippet' in item else "" )
        else:
            yield item['link']