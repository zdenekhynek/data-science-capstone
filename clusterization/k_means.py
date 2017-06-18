import os
from sklearn.cluster import KMeans
from sklearn.externals import joblib

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


def fit_clusters(vector_matrix, num_clusters = 5, cache = True):
  global km

  # do we have cached model
  cached_model = get_cached_model()
  if cached_model:
    return cached_model

  # we don't have cache model, instatniate k means
  km = KMeans(n_clusters=num_clusters)
  km.fit(vector_matrix)

  # cache model?
  if cache:
    cache_model(km)

  return km
