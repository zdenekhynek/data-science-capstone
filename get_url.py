import requests
import simplejson as json


def get_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.content)

    return False
