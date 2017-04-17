from get_url import get_url

GUARDIAN_SEARCH_API = 'http://content.guardianapis.com/search'
SHOW_FIELDS = 'body'
PAGE_SIZE = 50


def get_guardian_search(query, api_key, page=1, from_date=False,
                        to_date=False):
    url = '%s?page-size=%s&show-fields=%s&q=%s&page=%s&api-key=%s' % (
        GUARDIAN_SEARCH_API, PAGE_SIZE, SHOW_FIELDS, query, page, api_key
    )

    if (from_date):
        url += '&from-date=%s' % (from_date)

    if (to_date):
        url += '&to-date=%s' % (to_date)

    print url

    return get_url(url)
