import os
from sklearn.cluster import KMeans
from sklearn.externals import joblib

from articles import articles

from tokenizer import tokenizer
from tokenizer.remove_html import remove_html
from tokenizer.stop_words import filter_stop_words
from tokenizer.stem_words import stem_words
from tokenizer.remove_punctuation import remove_punctuation

from vectorization import tf_idf


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
  # tokenize
  tokens = tokenizer.tokenize(text)

  # remove punctuation
  tokens = remove_punctuation(tokens)

  # stem
  tokens = stem_words(tokens)

  # to lowercase
  return tokens


# 1. get the documents
documents = articles.get_articles().limit(1)

# 2. get just body documents
texts = get_document_texts(documents)

# 3. remove html
texts = remove_html_from_texts(texts)

# 4. tf_idf
vectorizer, matrix = tf_idf.fit_texts(texts, tokenize_and_stem)
terms = vectorizer.get_feature_names()

# 5. k-means



# print('terms', terms)

# clusters = km.labels_.tolist()

# sort cluster centers by proximity to centroid
# order_centroids = km.cluster_centers_.argsort()[:, ::-1]

# print(order_centroids)
