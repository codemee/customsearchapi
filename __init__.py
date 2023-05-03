GOOGLE_API_KEY = ''
GOOGLE_ID = ''

import requests

class ResultObj:
    def __init__(self, title, link, description):
        self.title = title
        self.url = link
        self.description = description
    
def search(query, num_results=10):
    url = 'https://www.googleapis.com/customsearch/v1?' \
          f'key={GOOGLE_API_KEY}&' \
          f'cx={GOOGLE_ID}&' \
          f'num={num_results}&' \
          f'q={query}'
    json = requests.get(url).json()
    results = []
    for item in json['items']:
        results.append(ResultObj(
            item['title'], 
            item['link'], 
            item['snippet'] if 'snippet' in item else "" ))

    return results