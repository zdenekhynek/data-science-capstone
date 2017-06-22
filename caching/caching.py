from pymongo import MongoClient
from sklearn.externals import joblib
import uuid

from database import DB_NAME, CACHE_COLLECTION_NAME


CACHE_FOLDER = 'data/cache'


def get_collection(db_name=DB_NAME, collection_name=CACHE_COLLECTION_NAME):
    client = MongoClient()
    db = client[db_name]
    collection = db[collection_name]
    return collection


def store_result(query, obj):
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
    collection = get_collection()
    result = collection.find_one(query)

    if not result:
        return False

    # found cache
    cache_file_path = result['cache_file_path']

    # load cache file
    return joblib.load(cache_file_path)
