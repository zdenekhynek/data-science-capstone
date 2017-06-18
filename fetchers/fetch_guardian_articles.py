from fetchers import fetch_url

GUARDIAN_SEARCH_API = 'http://content.guardianapis.com/search'
SHOW_FIELDS = 'body'
PAGE_SIZE = 50


def create_guardian_search_url(api_key, query, page, from_date, to_date):
    # format base url
    url = '%s?page-size=%s&show-fields=%s&q=%s&page=%s&api-key=%s' % (
        GUARDIAN_SEARCH_API, PAGE_SIZE, SHOW_FIELDS, query, page, api_key
    )

    if (from_date):
        url += '&from-date=%s' % (from_date)

    if (to_date):
        url += '&to-date=%s' % (to_date)

    print(url)

    return url


def fetch(api_key, query, page=1, from_date=False, to_date=False):
    url = create_guardian_search_url(api_key, query, page, from_date, to_date)
    request_response = fetch_url.fetch(url)

    if (request_response):
        return request_response['response']
    else:
        return False
