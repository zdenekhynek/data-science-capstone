from collections import Counter
import pandas as pd
import argparse

from articles import articles

from tokenizer import tokenizer
from tokenizer.remove_html import remove_html
from tokenizer.stop_words import filter_stop_words
from tokenizer.stem_words import stem_words
from tokenizer.remove_punctuation import remove_punctuation

from vectorization import tf_idf

from clusterization import k_means, truncated_svd

from visualisation.text_visualisation import print_cluster_keywords_and_titles, result_file_path
from visualisation.pca_scatter import plot_scatter, default_image_path

# CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--limit', help='Number of articles', default=10)
parser.add_argument('-c', '--clusters', help='Number of clusters', default=5)
cli_args = parser.parse_args()
cli_limit = int(cli_args.limit)
cli_clusters = int(cli_args.clusters)

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
documents = articles.get_articles().limit(cli_limit)
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
file_path = k_means.model_file_path.replace('.pkl', '_limit_' + str(cli_limit) + '.pkl')
cluster_model = k_means.fit_clusters(matrix, cli_clusters, file_path)
clusters = cluster_model.labels_

df = pd.DataFrame(articles)
df['cluster'] = clusters

file_path = result_file_path.replace('.txt', '_limit_' + str(cli_limit) + '.txt')
print_cluster_keywords_and_titles(df, cluster_model, vectorizer, file_path)

# 6. PCA
xs_ys = truncated_svd.fit_transform(matrix)
df['x'] = xs_ys[:,0]
df['y'] = xs_ys[:,1]
file_path = default_image_path.replace('.png', '_limit_' + str(cli_limit) + '.png')
plot_scatter(df, file_path)

print(xs_ys)

# print(ordered_centroids[0][1])
# print(tokens[ordered_centroids[0][2]])
# [print(document) for document in documents]
# print(clusters)
# print(cluster_model.cluster_centers_.shape)
