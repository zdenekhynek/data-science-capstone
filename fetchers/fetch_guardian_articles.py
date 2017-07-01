from fetchers import fetch_url

# endpoint API
GUARDIAN_SEARCH_API = 'http://content.guardianapis.com/search'

# which field to include in the response
SHOW_FIELDS = 'body'

# how many items per request
PAGE_SIZE = 50


def create_guardian_search_url(api_key, query, page, from_date, to_date):
    """
    Constructs the url for the GUARDIAN API endpoint with all the correct
    paramaters
    """

    # format base url
    url = '%s?page-size=%s&show-fields=%s&q=%s&page=%s&api-key=%s' % (
        GUARDIAN_SEARCH_API, PAGE_SIZE, SHOW_FIELDS, query, page, api_key
    )

    # add from-date query, if exists
    if (from_date):
        url += '&from-date=%s' % (from_date)

    # add to-date query, if exists
    if (to_date):
        url += '&to-date=%s' % (to_date)

    return url


def fetch(api_key, query, page=1, from_date=False, to_date=False):
    """
    Fetches articles from the GUARDIAN API with passed parameters
    """

    # construct url
    url = create_guardian_search_url(api_key, query, page, from_date, to_date)

    # do the fetch request
    request_response = fetch_url.fetch(url)

    # did we get a response
    if (request_response):
        return request_response['response']
    else:
        return False
