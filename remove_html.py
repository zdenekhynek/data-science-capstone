from BeautifulSoup import BeautifulSoup


def remove_html(raw_html):
    return BeautifulSoup(raw_html).text
