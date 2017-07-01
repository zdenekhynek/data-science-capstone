import requests
import simplejson as json


def fetch(url):
    """
    Make a request to the passed url, using the requests library
    """
    response = requests.get(url)

    # was the request sucessful
    if response.status_code == 200:
        return json.loads(response.content)

    return False
