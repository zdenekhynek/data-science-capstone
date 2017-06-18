TEXT_VISUALISATION_FILE_PATH = 'data/cluster_keywords_titles.txt'


def store_results(string, file_path):
    with open(file_path, 'w') as f:
        f.write(string)
        f.close()


def print_cluster_keywords_and_titles(articles, cluster_model, vectorizer,
                                      result_file=TEXT_VISUALISATION_FILE_PATH):
    result = ''

    feature_names = vectorizer.get_feature_names()

    ordered_centroids = cluster_model.cluster_centers_.argsort()[::-1]
    num_clusters = ordered_centroids.shape[0]

    # print out words
    for i in range(num_clusters):
        result += 'Cluster {0}:'.format(i) + '\n'
        cluster_centroid = ordered_centroids[i]
        top_10_indices = cluster_centroid[:10]

        result += 'Words:' + '\n'
        words = []
        for index in top_10_indices:
            words.append(feature_names[index])

    result += ''.join(words) + '\n\n'

    # print out titles
    grouped_articles = articles.groupby(by='cluster')
    for index, group in grouped_articles:
        result += 'Cluster {0}'.format(index) + '\n'
        result += group['webTitle'].to_string() + '\n\n'

    store_results(result, result_file)
