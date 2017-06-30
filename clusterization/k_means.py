from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from caching import caching

CACHE_OPERATION_KEY = 'k-means'


def fit_clusters(vector_matrix, num_clusters=5, cache_params={}):
    params = cache_params.copy()
    params['operation'] = CACHE_OPERATION_KEY
    params['num_clusters'] = num_clusters

    # do we have cached model?
    cached_model = caching.get_results(params)
    if cached_model:
        print('K-Means using cached model')
        return cached_model

    print('K-Means computing model')

    # we don't have cache model, instatniate k means
    km = KMeans(n_clusters=num_clusters)
    km.fit(vector_matrix)

    # cache model
    caching.store_result(params, km)

    return km


def print_silhouette_score(matrix, clusters, n_clusters):
    silhouette_avg = silhouette_score(matrix, clusters)
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg)
