from get_url import get_url

GUARDIAN_SEARCH_API = 'http://content.guardianapis.com/search'
SHOW_FIELDS = 'body'
PAGE_SIZE = 50


def get_guardian_search(query, api_key, page=1):
    url = '%s?page_size=%s&show-fields=%s&q=%s&page=%s&api-key=%s' % (
        GUARDIAN_SEARCH_API, PAGE_SIZE, SHOW_FIELDS, query, page, api_key
    )

    print url

    return get_url(url)

    #   scrape_guardian.py
    #   api-key
    #   show-fields
