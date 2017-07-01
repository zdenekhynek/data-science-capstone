import os

from pymongo import MongoClient

# grab connection string from an environment variable
mongodb_uri = os.environ['MONGODB_URI']

# make connection to mongodb instance
client = MongoClient(mongodb_uri)
