import os
from pymongo import MongoClient
import time
import argparse

from get_guardian_search import get_guardian_search

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


def insert_articles(articles, query):
    map(insert_article, articles)


def get_articles(page, query='', from_date=False, to_date=False):
    request_response = get_guardian_search(query, api_key, page, from_date,
                                           to_date)

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
            get_articles(page + 1, query, from_date, to_date)

    else:
        print 'Nothing found'


if __name__ == '__main__':
    # add CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query', help='Query to search for',
                        default='')
    parser.add_argument('-f', '--from_date', help='From date to search for',
                        default='')
    parser.add_argument('-t', '--to_date', help='To date to search for',
                        default='')
    args = parser.parse_args()

    get_articles(1, args.query, args.from_date, args.to_date)
