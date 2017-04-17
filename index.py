import os

from get_guardian_search import get_guardian_search
from pymongo import MongoClient
import time

api_key = os.environ['GUARDIAN_API_KEY']
q = 'terrorist'

client = MongoClient()
db = client['capstone']

articles_collection = db.articles


def insert_article(article):
    # using update to avoid duplication
    query = {'id': article['id']}

    # add for which query article was returned
    article['query'] = q

    print 'Inserting id: %s' % (article['id'])
    articles_collection.update(
        query,
        article,
        True
    )


def insert_articles(articles):
    map(insert_article, articles)


def get_articles(page):
    request_response = get_guardian_search(q, api_key, page)

    if (request_response and request_response['response']['results']):
        articles = request_response['response']['results']
        pages = int(request_response['response']['pages'])

        print 'Receive %s page from %s pages' % (page, pages)

        #   store results
        insert_articles(articles)

        #   should we load additional articles?
        if (pages and page < pages):
            #   load next article
            time.sleep(1)
            get_articles(page + 1)

    else:
        print 'Nothing found'


if __name__ == '__main__':
    get_articles(1)
