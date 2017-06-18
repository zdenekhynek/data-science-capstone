from sklearn.decomposition import PCA

default_number_of_components = 2

pca = False

def fit_transform(data, num_components = default_number_of_components):
  global pca

  pca = PCA(n_components = num_components)
  pca_transformed = pca.fit_transform(data)

  # print(pca.explained_variance_ratio_)

  return pca_transformed
