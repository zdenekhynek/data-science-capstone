from database import DB_NAME, ARTICLES_COLLECTION_NAME
from database.client import client


def get_collection(db_name=DB_NAME, collection_name=ARTICLES_COLLECTION_NAME):
    db = client[db_name]
    collection = db[collection_name]
    return collection


def get_articles(query={}):
    collection = get_collection()
    return collection.find(query)


def get_document_texts(documents):
    return [document['fields']['body'] for document in documents]


def get_document_titles(documents):
    return [document['webTitle'] for document in documents]
