from sklearn.decomposition import PCA

from caching import caching

CACHE_OPERATION_KEY = 'pca'
NUMBER_OF_COMPONENTS = 2

pca = False


def fit_transform(data, num_components=NUMBER_OF_COMPONENTS, cache_params={}):
    global pca

    params = cache_params.copy()
    params['operation'] = CACHE_OPERATION_KEY
    params['num_components'] = num_components

    pca = PCA(n_components=num_components)
    pca_transformed = pca.fit_transform(data)

    # print(pca.explained_variance_ratio_)

    result = (pca, pca_transformed)
    caching.store_result(params, result)

    return result
