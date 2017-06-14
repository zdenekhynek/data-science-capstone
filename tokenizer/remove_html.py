from bs4 import BeautifulSoup


def remove_html(raw_html):
    return BeautifulSoup(raw_html, 'html.parser').text
