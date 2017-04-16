import os

from get_guardian_search import get_guardian_search
from pymongo import MongoClient

api_key = os.environ['GUARDIAN_API_KEY']
query = 'terrorist'

client = MongoClient()
db = client['capstone']

articles_collection = db.articles



print get_guardian_search(query, api_key)
