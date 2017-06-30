import uuid

from sklearn.externals import joblib

from database import DB_NAME, CACHE_COLLECTION_NAME
from database.client import client

CACHE_FOLDER = 'data/cache'
ENABLED = False


def get_collection(db_name=DB_NAME, collection_name=CACHE_COLLECTION_NAME):
    db = client[db_name]
    collection = db[collection_name]
    return collection


def store_result(query, obj):
    if not ENABLED:
        return

    # get random file
    filename = str(uuid.uuid4())

    # store result into file using joblib
    full_filename = CACHE_FOLDER + '/' + filename
    joblib.dump(obj, full_filename)

    # update record in database
    collection = get_collection()

    # result
    result = query.copy()
    result['cache_file_path'] = full_filename
    collection.update(query, result, True)


def get_results(query):
    if not ENABLED:
        return False

    collection = get_collection()
    result = collection.find_one(query)

    if not result:
        return False

    # found cache
    cache_file_path = result['cache_file_path']

    # load cache file
    return joblib.load(cache_file_path)
