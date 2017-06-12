import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

from articles import articles
from remove_html import remove_html
from tokenizer import tokenizer
from stop_words import filter_stop_words
from stem_words import stem_words
from sklearn.externals import joblib

def get_document_texts(documents):
  texts = []

  for document in documents:
    text = document['fields']['body']
    texts.append(text)

  return texts


def remove_html_from_texts(texts):
  return list(
    map(remove_html, texts)
  )


def tokenize_and_stem(text):
  tokenized = tokenizer.tokenize(text)
  stemmed = stem_words(tokenized)
  return stemmed


# 1. get the documents
documents = articles.get_articles().limit(100)

# 2. get just body documents
texts = get_document_texts(documents)

# 3. remove html
texts = remove_html_from_texts(texts)


# 3. tokenize + 4. stop word + 5. stemming + 6. tf-idf
tf_idf_vectorizer = TfidfVectorizer(
  stop_words='english',
  use_idf=True,
  tokenizer=tokenize_and_stem,
  ngram_range=(1,3)
)

tf_idf_matrix = tf_idf_vectorizer.fit_transform(texts)
terms = tf_idf_vectorizer.get_feature_names()

# 7. k-means

# see if we already have the model
model_file_path = 'k_means_clusters.pkl'

km = False

if (os.path.exists(model_file_path)):
  print('loading saved model')
  km = joblib.load(model_file_path)
else:
  print('recreating model')
  num_clusters = 5
  km = KMeans(n_clusters=num_clusters)
  km.fit(tf_idf_matrix)

  # save result
  joblib.dump(km, model_file_path)


# print('terms', terms)

# clusters = km.labels_.tolist()

# sort cluster centers by proximity to centroid
# order_centroids = km.cluster_centers_.argsort()[:, ::-1]

# print(order_centroids)
