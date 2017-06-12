import os
import argparse
from pymongo import MongoClient

from articles import articles
from fetchers import fetch_articles


def insert_document_to_mongo(collection, document):
  query = {'id': document['id']}
  collection.update(query, document, True)


def insert_documents_to_mongo(collection, documents):
  for document in documents:
    insert_document_to_mongo(collection, document)


def on_fetch_complete(documents):
  collection = articles.get_collection(DB_NAME, COLLECTION_NAME)
  insert_documents_to_mongo(collection, documents)


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

    # search params
    api_key = os.environ['GUARDIAN_API_KEY']
    q = 'terrorist'

    fetch_articles.fetch(on_fetch_complete, api_key, q, 1)
