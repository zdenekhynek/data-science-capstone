from pipeline import run_pipeline

parameters = {
    'documents': {
        'query': {},
        'limit': 10
    },
    'tf_idf': {
        'ngram_range': (1, 2),
        'min_df': 2,
        'max_df': 1.0,
        'max_features': None
    },
    'k_means': {
        'n_clusters': 5,
        'max_iter': 300
    },
    'truncated_svd': {
        'n_components': 2,
        'n_iter': 5
    }
}

run_pipeline(parameters)

# cluster_range = range(6, 10)
# print(cluster_range)

# for n_clusters in range(6, 10):
#    parameters['k_means']['n_clusters'] = n_clusters
#    run_pipeline(parameters)
