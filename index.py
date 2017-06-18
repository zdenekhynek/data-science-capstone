from collections import Counter
import pandas as pd

from articles import articles

from tokenizer import tokenizer
from tokenizer.remove_html import remove_html
from tokenizer.stop_words import filter_stop_words
from tokenizer.stem_words import stem_words
from tokenizer.remove_punctuation import remove_punctuation

from vectorization import tf_idf

from clusterization import k_means

from visualisation.text_visualisation import print_cluster_keywords_and_titles


# options
NUMBER_OF_ARTICLES = 10


def get_document_texts(documents):
  return [document['fields']['body'] for document in documents]


def remove_html_from_texts(texts):
  return [remove_html(text) for text in texts]


def tokenize_and_stem(text):
  # tokenize
  tokens = tokenizer.tokenize(text)

  # remove punctuation
  tokens = remove_punctuation(tokens)

  # stem
  tokens = stem_words(tokens)

  # to lowercase
  return tokens


def most_common_tokens(texts):
  tokens = [token for text in texts for token in tokenize_and_stem(text)]
  filtered_tokens = filter_stop_words(tokens)
  counter = Counter(filtered_tokens)
  return counter.most_common(10)


def most_important_tokens(vectorizer):
  tokens = dict(zip(vectorizer.get_feature_names(), vectorizer.idf_))
  df = pd.DataFrame(columns=['tfidf']).from_dict(tokens, orient='index')
  df.columns = ['tfidf']
  df = df.sort_values(by=['tfidf'], ascending=False)
  return df.head(30)


# 1. get the documents
documents = articles.get_articles().limit(NUMBER_OF_ARTICLES)
articles = [document for document in documents]

# 2. get just body documents
texts = get_document_texts(articles)

# 3. remove html
texts = remove_html_from_texts(texts)

# find out most common words
keywords = most_common_tokens(texts)
# print('Keywords', keywords)

# 4. tf_idf
vectorizer, matrix = tf_idf.fit_texts(texts, tokenize_and_stem)
terms = vectorizer.get_feature_names()

important_tokens = most_important_tokens(vectorizer)
# print('Most important tokens', important_tokens)

# 5. k-means
cluster_model = k_means.fit_clusters(matrix)
clusters = cluster_model.labels_

df = pd.DataFrame(articles)
df['cluster'] = clusters

print_cluster_keywords_and_titles(df, cluster_model, vectorizer)

# print(ordered_centroids[0][1])
# print(tokens[ordered_centroids[0][2]])
#[print(document) for document in documents]
# print(clusters)
# print(cluster_model.cluster_centers_.shape)
