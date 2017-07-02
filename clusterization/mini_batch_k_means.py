from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import silhouette_score

from caching import caching

# key under which the operation result will be stored in the cache collection
CACHE_OPERATION_KEY = 'mini-batch-k-means'


def fit_clusters(vector_matrix, params={}):
    """
    Calculates given number of clusters using mini-batch-k-means.
    Comparing to k-means, should be faster for datasets with more then 10000
    datapoints
    http://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html
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

    # we don't have cache model, instatniate mini batch k means
    km = MiniBatchKMeans(n_clusters=params['n_clusters'],
                         max_iter=params['max_iter'])
    # fit matrix
    km.fit(vector_matrix)

    # cache model
    caching.store_result(params, km)

    return km


def get_silhouette_score(matrix, clusters):
    """
    Calculates silhouette score and return results
    """
    return silhouette_score(matrix, clusters)


def print_silhouette_score(matrix, clusters, n_clusters):
    """
    Calculates silhouette score and displays results
    """
    silhouette_avg = silhouette_score(matrix, clusters)
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg)


def get_clusters_tokens(cluster_model, vectorizer):
    """
    Returns sorted tokens (sorted by on distance from a cluster center) for
    each cluster
    """

    # get all tokens from tf-idf matrix
    feature_names = vectorizer.get_feature_names()

    # get indices of tokens for each cluster,
    # sorted by distance from the cluster center
    ordered_indices = cluster_model.cluster_centers_.argsort()[::-1]

    # how many clusters are we dealing with
    num_clusters = ordered_indices.shape[0]

    clusters = []
    for i in range(num_clusters):
        # get token indices for each cluster
        cluster_order_indices = ordered_indices[i]

        # retrieve the actual tokens for each index
        tokens = []
        for index in cluster_order_indices:
            tokens.append(feature_names[index])

        clusters.append(tokens)

    return clusters
