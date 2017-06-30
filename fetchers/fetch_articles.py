import time

from fetchers import fetch_guardian_articles

IN_BETWEEN_REQUESTS_GAP = 1


def add_query_to_article(article, query=''):
    article['query'] = query
    return article


def fetch_articles(api_key, query, page, from_date, to_date, collection=[]):
    response = fetch_guardian_articles.fetch(api_key, query, page,
                                             from_date, to_date)

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
    fetch_articles(api_key, query, page, from_date, to_date)
