# use Truncated SVG when you have sparse input
# e.g. from vectorization
from sklearn.decomposition import TruncatedSVD

CACHE_OPERATION_KEY = 'truncated-svd'
NUMBER_OF_COMPONENTS = 2


def fit_transform(data, params={}):
    # params = cache_params.copy()
    # params['operation'] = CACHE_OPERATION_KEY
    # params['num_components'] = num_components

    # do we have cached model?
    # cached_model = caching.get_results(params)
    # if cached_model:
    #    print('Truncated SVD using cached model')
    #    return cached_model

    # print('Truncated SVD computing model')

    svd = TruncatedSVD(n_components=params['n_components'])
    svd_transformed = svd.fit_transform(data)

    # print(svd.explained_variance_ratio_)

    # cache result
    result = (svd, svd_transformed)
    # caching.store_result(params, result)

    return result
