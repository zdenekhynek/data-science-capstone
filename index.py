import argparse
import time

import pandas as pd
from collections import Counter

from articles import articles
from tokenizer import tokenizer
from tokenizer.remove_html import remove_html
from tokenizer.stop_words import filter_stop_words
from tokenizer.stem_words import stem_words
from tokenizer.remove_punctuation import remove_punctuation
from vectorization import tf_idf
from clusterization import k_means, mini_batch_k_means, truncated_svd
from topics import lda
from visualisation.text_visualisation import print_cluster_keywords_and_titles, TEXT_VISUALISATION_FILE_PATH
from visualisation.pca_scatter import plot_scatter, PCA_SCATTER_FILE_PATH
from visualisation.lda_topics import print_lda_topics, LDA_TOPIC_FILE_PATH
from caching import caching


# CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--limit', help='Number of articles', default=10)
parser.add_argument('-c', '--clusters', help='Number of clusters', default=5)
cli_args = parser.parse_args()
cli_limit = int(cli_args.limit)
cli_clusters = int(cli_args.clusters)


cache_params = {'limit': cli_limit}


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

####################################################
# 1. get the documents a process them
####################################################

documents = articles.get_articles().limit(cli_limit)
article_docs = [document for document in documents]

print('1. Getting articles', time.process_time() - t)
t = time.process_time()

# 2. get just body documents
texts = articles.get_document_texts(article_docs)

print('2. Get just body documents', time.process_time() - t)
t = time.process_time()


# 3. remove html
texts = [remove_html(text) for text in texts]

print('3. Remove HTML', time.process_time() - t)
t = time.process_time()

# find out most common words
# keywords = most_common_tokens(texts)
# print('Keywords', keywords)


####################################################
# 4. tf_idf
####################################################

ngrams = (1, 1)
vectorizer, matrix = tf_idf.fit_texts(texts, tokenize_and_stem, ngrams,
                                      'english', cache_params)

# terms = vectorizer.get_feature_names()
# important_tokens = most_important_tokens(vectorizer)
# print('Most important tokens', important_tokens)

print('4. TF-IDF', time.process_time() - t)
t = time.process_time()


####################################################
# 5. k-means
####################################################

kmeans_cache_params = cache_params.copy()
kmeans_cache_params['ngrams'] = ngrams
cluster_model = mini_batch_k_means.fit_clusters(matrix, cli_clusters, kmeans_cache_params)
clusters = cluster_model.labels_
k_means.print_silhouette_score(matrix, clusters, cli_clusters)

print('5. K-Means', time.process_time() - t)
t = time.process_time()


####################################################
# 6. PCA
####################################################

svd, xs_ys = truncated_svd.fit_transform(matrix, 2, cache_params)

print('6. PCA', time.process_time() - t)
t = time.process_time()

df = pd.DataFrame(article_docs)
df['cluster'] = clusters
df['x'] = xs_ys[:, 0]
df['y'] = xs_ys[:, 1]

# cache data frame
df_cache_params = cache_params.copy()
df_cache_params['operation'] = 'df'
df_cache_params['num_clusters'] = cli_clusters
caching.store_result(df_cache_params, df)


####################################################
# Plotting results
####################################################

# replace_string = '__num_clusters__{0}__limit__{1}.png'.format(str(cli_clusters), str(cli_limit))
# file_path = PCA_SCATTER_FILE_PATH.replace('.png', replace_string)

# plot_scatter(df, file_path)

# print('6b. Plotting PCA', time.process_time() - t)
# t = time.process_time()

replace_string = '__num_clusters__{0}__limit__{1}.txt'.format(str(cli_clusters), str(cli_limit))
file_path = TEXT_VISUALISATION_FILE_PATH.replace('.txt', replace_string)

print_cluster_keywords_and_titles(df, cluster_model, vectorizer, file_path)

print('5b. Visualisating keywords', time.process_time() - t)
t = time.process_time()

# 7. LDA
# tokenize
# tokenized_texts = [tokenize_and_stem(text) for text in texts]

# remove stop word
# tokens = [filter_stop_words(text) for text in tokenized_texts]

# fitted_lda = lda.fit_model(tokens)
# replace_string = '__num_clusters__{0}__limit__{1}.txt'
# .format(str(cli_clusters), str(cli_limit))
# file_path = LDA_TOPIC_FILE_PATH.replace('.txt', replace_string)
# print_lda_topics(fitted_lda, file_path)

# print('7. LDA', time.process_time() - t)
