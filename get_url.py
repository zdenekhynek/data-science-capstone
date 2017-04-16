import requests


def get_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.content

    return False
