import time

from fetchers import fetch_guardian_articles

# gap between API requests in seconds
IN_BETWEEN_REQUESTS_GAP = 1


def add_query_to_article(article, query=''):
    """
    Store query with the article so that we can track from which request the
    article has been retrieved (e.g. query for terrorism related articles)
    """
    article['query'] = query
    return article


def fetch_articles(api_key, query, page, from_date, to_date, collection=[]):
    """
    Fetch articles from the GUARDIAN API for specified query, page and from
    and to date. Unless fetched all articles, will call recursively itself
    to retrieve all the results from a paginated API
    """

    # fetch articles
    response = fetch_guardian_articles.fetch(api_key, query, page,
                                             from_date, to_date)

    # do we have results?
    if (response and response['results']):
        articles = response['results']

        # add for which query the article
        # make sure we convert result of map to list
        # https://stackoverflow.com/questions/1303347/getting-a-map-to-return-a-list-in-python-3-x
        articles = list(
            map(
                lambda article: add_query_to_article(article, query),
                articles
            )
        )

        # concatenate
        collection = collection + articles

        #   should we fetch additional articles?
        pages = response['pages']
        if (pages and page < pages):
            #   load next article
            time.sleep(IN_BETWEEN_REQUESTS_GAP)
            fetch_articles(api_key, query, page + 1,
                           from_date, to_date, collection)
        else:
            # all done, return collected articles
            return collection
    else:
        print('Nothing found')


def fetch(api_key, query='', page=1, from_date=False, to_date=False):
    """
    Fetch all articles from a paginated GUARDIAN API
    """
    fetch_articles(api_key, query, page, from_date, to_date)
