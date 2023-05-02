# A simple Python module for Custom Search JSON API

There're many Python modules that scrapting the google search pages to get results. They may violate the policy of Google and also make too many requests to Google. This module use the Google official custom search JSON API with the limitation of 100 requests/day for free.

## Prerequisites

- Get Search engine ID in [Programmable Search Engine control panel](https://programmablesearchengine.google.com/controlpanel/all).

- Get API key at [Custom Search JSON API](https://developers.google.com/custom-search/v1/overview#api_key).

## Usage:

1. Import the module, setting API key and ID:

    ```python
    import customsearchapi
    customsearchapi.GOOGLE_API_KEY = 'GOOGLE API KEY'
    customsearchapi.GOOGLE_ID = 'Google Search Engine ID'
    ```

2. Call the search function to search, this will return a list of ResultObj objects each with link, title, descrition attributes:

    ```python
    for i in customsearchapi.search('python', num_results=2):
        print(i.link)
        print(i.title)
        print(i.description)
        print("")
    ```
    the result shows bellow:

    ```
    https://www.python.org/
    Welcome to Python.org
    The official home of the Python Programming Language.

    https://www.w3schools.com/python/
    Python Tutorial
    Learn Python. Python is a popular programming language. Python can be used on a server to create web applications. Start learning Python now » ...
    ```
3. if ommit the `num_results`, default to 10.
