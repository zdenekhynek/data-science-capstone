from pymongo import MongoClient

DB_NAME = 'capstone'
COLLECTION_NAME = 'articles'


def get_collection(db_name = DB_NAME, collection_name = COLLECTION_NAME):
  client = MongoClient()
  db = client[db_name]
  collection = db[collection_name]
  return collection


def get_articles(query = {}):
  collection = get_collection()
  return collection.find(query)


def get_document_texts(documents):
  return [document['fields']['body'] for document in documents]
