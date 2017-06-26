import argparse
import time

import pandas as pd
from collections import Counter

from articles import articles
from performance.benchmarks import Benchmarks
from tokenizer import tokenizer
from tokenizer.remove_html import remove_html
from tokenizer.tokenize_and_stem import tokenize_and_stem
from tokenizer.get_tokens import get_texts_tokens
from vectorization import tf_idf
from vectorization.get_weighted_tokens import get_weighted_tokens
from clusterization import k_means, mini_batch_k_means, truncated_svd
from topics import lda
from visualisation.text_visualisation import print_cluster_keywords_and_titles, TEXT_VISUALISATION_FILE_PATH
from visualisation.lda_topics import print_lda_topics, LDA_TOPIC_FILE_PATH
from results import results


def run_pipeline(parameters={}):
    benchmarks = Benchmarks()

    ####################################################
    # 1. get the documents a process them
    ####################################################

    doc_params = parameters['documents']
    documents = articles.get_articles(doc_params['query']).limit(doc_params['limit'])
    article_docs = [document for document in documents]
    benchmarks.add_benchmark('1-get-articles')

    # 1a. get just body documents
    texts = articles.get_document_texts(article_docs)
    benchmarks.add_benchmark('2-get-body-documents')

    # 1b. remove html
    texts = [remove_html(text) for text in texts]
    benchmarks.add_benchmark('3-remove-html')

    # STORING 1 - store tokens
    results.store_tokens(parameters, get_texts_tokens(texts))

    ####################################################
    # 4. tf_idf
    ####################################################

    vectorizer, matrix = tf_idf.fit_texts(texts, tokenize_and_stem,
                                          parameters['tf_idf'])
    benchmarks.add_benchmark('4-tf-idf')

    # STORING 2 - store tokens with tf-idf
    results.store_idf_tokens(parameters, get_weighted_tokens(vectorizer))

    ####################################################
    # 5. k-means
    ####################################################

    cluster_model = mini_batch_k_means.fit_clusters(matrix, parameters['k_means'])
    benchmarks.add_benchmark('5-mini-batch-k-means')

    # STORING 3 - store cluster tokens
    cluster_tokes = mini_batch_k_means.get_clusters_tokens(cluster_model,
                                                           vectorizer)
    results.store_cluster_tokes(parameters, cluster_tokes)

    clusters = cluster_model.labels_
    silhouette_score = mini_batch_k_means.get_silhouette_score(matrix, clusters)

    # STORING 4 - store results
    results.store_clusterisation_results(parameters, silhouette_score)

    ####################################################
    # 6. PCA
    ####################################################

    svd, xs_ys = truncated_svd.fit_transform(matrix, parameters['truncated_svd'])
    benchmarks.add_benchmark('6-pca')

    df = pd.DataFrame(article_docs)
    df['cluster'] = clusters
    df['x'] = xs_ys[:, 0]
    df['y'] = xs_ys[:, 1]

    # STORING 5 - store clusters and PCA results
    results.store_cluster_articles(parameters, df)

    # STORING 6 - store benchmarks
    results.store_performance(parameters, benchmarks.get_benchmarks())
