from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from caching import caching

# key under which the operation result will be stored in the cache collection
CACHE_OPERATION_KEY = 'k-means'


def fit_clusters(vector_matrix, num_clusters=5, cache_params={}):
    """
    Calculates given number of clusters using k-means
    http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
    """

    # construct cache query object to find out if we've run this operation
    # already and might be able to use cached results instead (saves time)
    params = cache_params.copy()
    params['operation'] = CACHE_OPERATION_KEY
    params['num_clusters'] = num_clusters

    # do we have cached model?
    cached_model = caching.get_results(params)
    if cached_model:
        return cached_model

    # we don't have cache model, instatniate k means
    km = KMeans(n_clusters=num_clusters)

    # fit matrix
    km.fit(vector_matrix)

    # cache model
    caching.store_result(params, km)

    return km


def print_silhouette_score(matrix, clusters, n_clusters):
    """
    Calculates silhouette score and displays results
    """
    silhouette_avg = silhouette_score(matrix, clusters)
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg)
