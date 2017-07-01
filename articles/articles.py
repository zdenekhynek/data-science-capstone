from database import DB_NAME, ARTICLES_COLLECTION_NAME
from database.client import client


def get_collection(db_name=DB_NAME, collection_name=ARTICLES_COLLECTION_NAME):
    """
    Returns mongodb articles collection from specified database
    """
    db = client[db_name]
    collection = db[collection_name]
    return collection


def get_articles(query={}):
    """
    Perfors mongodb find query on the articles collection
    """
    collection = get_collection()
    return collection.find(query)


def get_document_texts(documents):
    """
    Returns a list of article contents from nested objects
    """
    return [document['fields']['body'] for document in documents]


def get_document_titles(documents):
    """
    Returns a list of titles from documents
    """
    return [document['webTitle'] for document in documents]
