import os
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn.metrics import silhouette_score

# see if we already have the model
model_file_path = 'data/k_means_clusters.pkl'

km = False

def has_cached_model(cache_path = model_file_path):
  return os.path.exists(cache_path)


def get_cached_model(cache_path = model_file_path):
  if has_cached_model(cache_path):
    # return cached fited model
    return joblib.load(cache_path)
  else:
    return False


def cache_model(model, cache_path = model_file_path):
  joblib.dump(model, cache_path)


def fit_clusters(vector_matrix, num_clusters = 5, cache_path = model_file_path):
  global km

  # do we have cached model
  if cache_path:
    cached_model = get_cached_model(cache_path)
    if cached_model:
      return cached_model

  # we don't have cache model, instatniate k means
  km = KMeans(n_clusters=num_clusters)
  km.fit(vector_matrix)

  # cache model?
  if cache_path:
    cache_model(km, cache_path)

  return km


def print_silhouette_score(matrix, clusters, n_clusters):
  silhouette_avg = silhouette_score(matrix, clusters)
  print("For n_clusters =", n_clusters, "The average silhouette_score is :", silhouette_avg)
