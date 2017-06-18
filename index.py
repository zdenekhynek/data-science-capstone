import pandas as pd
import argparse
import time
from collections import Counter

from articles import articles

from tokenizer import tokenizer
from tokenizer.remove_html import remove_html
from tokenizer.stop_words import filter_stop_words
from tokenizer.stem_words import stem_words
from tokenizer.remove_punctuation import remove_punctuation

from vectorization import tf_idf

from clusterization import k_means, truncated_svd, lda

from visualisation.text_visualisation import print_cluster_keywords_and_titles, TEXT_VISUALISATION_FILE_PATH
from visualisation.pca_scatter import plot_scatter, PCA_SCATTER_FILE_PATH
from visualisation.lda_topics import print_lda_topics, LDA_TOPIC_FILE_PATH


# CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--limit', help='Number of articles', default=10)
parser.add_argument('-c', '--clusters', help='Number of clusters', default=5)
cli_args = parser.parse_args()
cli_limit = int(cli_args.limit)
cli_clusters = int(cli_args.clusters)


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


t = time.process_time()

# 1. get the documents
documents = articles.get_articles().limit(cli_limit)
article_docs = [document for document in documents]

print('1. Getting articles', time.process_time() - t)
t = time.process_time()

# 2. get just body documents
texts = articles.get_document_texts(article_docs)

# 3. remove html
texts = [remove_html(text) for text in texts]

print('3. Remove HTML', time.process_time() - t)
t = time.process_time()

# find out most common words
keywords = most_common_tokens(texts)
# print('Keywords', keywords)

# 4. tf_idf
vectorizer, matrix = tf_idf.fit_texts(texts, tokenize_and_stem)
terms = vectorizer.get_feature_names()

important_tokens = most_important_tokens(vectorizer)
print('Most important tokens', important_tokens)

print('4. TF-IDF', time.process_time() - t)
t = time.process_time()


# 5. k-means
cluster_model = k_means.fit_clusters(matrix, cli_clusters, { 'limit': cli_limit })
clusters = cluster_model.labels_
k_means.print_silhouette_score(matrix, clusters, cli_clusters)

print('5. K-Means', time.process_time() - t)

df = pd.DataFrame(article_docs)
df['cluster'] = clusters

file_path = TEXT_VISUALISATION_FILE_PATH.replace('.txt', '_limit_' + str(cli_limit) + '.txt')
print_cluster_keywords_and_titles(df, cluster_model, vectorizer, file_path)

# 6. PCA
t = time.process_time()
xs_ys = truncated_svd.fit_transform(matrix)
df['x'] = xs_ys[:,0]
df['y'] = xs_ys[:,1]
file_path = PCA_SCATTER_FILE_PATH.replace('.png', '_limit_' + str(cli_limit) + '.png')
plot_scatter(df, file_path)

print('6. PCA', time.process_time() - t)
t = time.process_time()


# 7. LDA
# tokenize
# tokenized_texts = [tokenize_and_stem(text) for text in texts]

# remove stop word
# tokens = [filter_stop_words(text) for text in tokenized_texts]

# fitted_lda = lda.fit_model(tokens)
# file_path = LDA_TOPIC_FILE_PATH.replace('.txt', '_limit_' + str(cli_limit) + '.txt')
# print_lda_topics(fitted_lda, file_path)

# print('7. LDA', time.process_time() - t)
