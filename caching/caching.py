import uuid
from os import path

from sklearn.externals import joblib

from database import DB_NAME, CACHE_COLLECTION_NAME
from database.client import client

# path to the cache folder, where all the cached files are stored
CACHE_FOLDER = 'data/cache'

# Flag to disable cache temporarily
ENABLED = False


def get_collection(db_name=DB_NAME, collection_name=CACHE_COLLECTION_NAME):
    """
    Return mongodb cache collection from specified database
    """
    db = client[db_name]
    collection = db[collection_name]
    return collection


def store_result(query, obj):
    """
    Stores passed object in a file and stores path to the file and query
    into the cache collection, so that the cached obj can be retrieved later on
    easily
    """

    # do not store anything if cache disabled
    if not ENABLED:
        return

    # proceed with caching the results

    # get random file name
    filename = str(uuid.uuid4())

    # store result into file using joblib
    full_filename = path.join(CACHE_FOLDER, filename)
    joblib.dump(obj, full_filename)

    # get cache collection
    collection = get_collection()

    # result
    result = query.copy()
    result['cache_file_path'] = full_filename

    # store record about the cached object into the collection
    collection.update(query, result, True)


def get_results(query):
    """
    Retrieves cached object, if the record with given query exists in the
    cache collection
    """

    # do not retrive anything if cache disabled
    if not ENABLED:
        return False

    # do we have cache record for given query?
    collection = get_collection()
    result = collection.find_one(query)

    if not result:
        # nothing cached for given query
        return False

    # found cache

    # get path to the cached object
    cache_file_path = result['cache_file_path']

    # load cache file
    return joblib.load(cache_file_path)
