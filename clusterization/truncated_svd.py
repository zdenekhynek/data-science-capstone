from sklearn.decomposition import TruncatedSVD

from caching import caching

# key under which the operation result will be stored in the cache collection
CACHE_OPERATION_KEY = 'truncated-svd'

# default number of components
NUMBER_OF_COMPONENTS = 2


def fit_transform(data, params={}):
    """
    Reduces data dimensions to a given number of components using Truncated SVD
    Unlike PCA, can be used for sparse input, e.g. from vectorization
    http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD
    """

    # construct cache query object to find out if we've run this operation
    # already and might be able to use cached results instead (saves time)
    params = cache_params.copy()
    params['operation'] = CACHE_OPERATION_KEY
    params['num_components'] = num_components

    # do we have cached model?
    cached_model = caching.get_results(params)
    if cached_model:
        return cached_model

    # we don't have cached model, init svd
    svd = TruncatedSVD(n_components=params['n_components'])

    # fit model and apply dimensionality reduction
    svd_transformed = svd.fit_transform(data)

    # construct result object (we're both orig model and fitter model
    # so that we could potentially access both)
    result = (svd, svd_transformed)
    caching.store_result(params, result)

    return result
