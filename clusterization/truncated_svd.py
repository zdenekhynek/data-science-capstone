# use Truncated SVG when you have sparse input
# e.g. from vectorization
#

from sklearn.decomposition import TruncatedSVD

default_number_of_components = 2

svd = False

def fit_transform(data, num_components = default_number_of_components):
  global svd

  svd = TruncatedSVD(n_components = num_components)
  svd_transformed = svd.fit_transform(data)

  # print(svd.explained_variance_ratio_)

  return svd_transformed
