# use Truncated SVG when you have sparse input
# e.g. from vectorization
from sklearn.decomposition import TruncatedSVD

from caching import caching

CACHE_OPERATION_KEY = 'truncated-svd'
NUMBER_OF_COMPONENTS = 2

svd = False


def fit_transform(data, num_components = NUMBER_OF_COMPONENTS, cache_params={}):
  global svd

  cache_params['operation'] = CACHE_OPERATION_KEY
  cache_params['num_components'] = num_components

  # do we have cached model?
  cached_model = caching.get_results(cache_params)
  if cached_model:
    print('Truncated SVD using cached model')
    return cached_model


  print('Truncated SVD computing model')

  svd = TruncatedSVD(n_components = num_components)
  svd_transformed = svd.fit_transform(data)

  # print(svd.explained_variance_ratio_)

  # cache result
  result = (svd, svd_transformed)
  caching.store_result(cache_params, result)

  return result
