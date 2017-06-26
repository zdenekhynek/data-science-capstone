from pipeline import run_pipeline


def run_single_pipeline(params):
    run_pipeline(params)


def run_cluster_range(range):
    for n_clusters in range:
        parameters['k_means']['n_clusters'] = n_clusters
        run_pipeline(parameters)


news_only_query = {'$or': [{'sectionId': 'world'}, {'sectionId': 'uk-news'}]}

parameters = {
    'documents': {
        'query': news_only_query,
        'limit': 1000
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
