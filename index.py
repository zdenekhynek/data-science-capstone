import os
from pymongo import MongoClient


from tokenize import tokenize
from stop_words import filter_stop_words
from remove_html import remove_html

# from geocode_text import geocode_text

# 1. collect articles
api_key = os.environ['GUARDIAN_API_KEY']

client = MongoClient()
db = client['capstone']

articles_collection = db.articles

# get only first one for testing
first = articles_collection.find().next()
body = first['fields']['body']

# 2. remove html
clean_body = remove_html(body)

# 3. tokenize
tokenized = tokenize(clean_body)

# 4. stop word removal
stop_removed = filter_stop_words(tokenized)

print stop_removed

# 5. stemming


# 6. tf-idf


# 7. geocode result
