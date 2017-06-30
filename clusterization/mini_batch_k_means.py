import os
from sklearn.cluster import MiniBatchKMeans
from sklearn.externals import joblib
from sklearn.metrics import silhouette_score

from caching import caching

CACHE_OPERATION_KEY = 'mini-batch-k-means'


def fit_clusters(vector_matrix, params={}):
    # params = cache_params.copy()
    # params['operation'] = CACHE_OPERATION_KEY
    # params['num_clusters'] = num_clusters

    # do we have cached model?
    # cached_model = caching.get_results(params)
    # if cached_model:
    #    print('K-Means using cached model')
    #    return cached_model

    # print('K-Means computing model')

    # we don't have cache model, instatniate k means
    km = MiniBatchKMeans(n_clusters=params['n_clusters'],
                         max_iter=params['max_iter'])
    km.fit(vector_matrix)

    # cache model
    # caching.store_result(params, km)

    return km


def get_silhouette_score(matrix, clusters):
    return silhouette_score(matrix, clusters)


def print_silhouette_score(matrix, clusters, n_clusters):
    silhouette_avg = silhouette_score(matrix, clusters)
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg)


def get_clusters_tokens(cluster_model, vectorizer):
    feature_names = vectorizer.get_feature_names()

    print('feature_names', feature_names)

    ordered_indices = cluster_model.cluster_centers_.argsort()[::-1]
    print('ordered_indices', ordered_indices)
    num_clusters = ordered_indices.shape[0]

    clusters = []

    for i in range(num_clusters):
        cluster_order_indices = ordered_indices[i]

        tokens = []
        for index in cluster_order_indices:
            tokens.append(feature_names[index])

        clusters.append(tokens)

    return clusters
