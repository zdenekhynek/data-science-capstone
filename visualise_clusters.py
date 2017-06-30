import os
import math

import pandas as pd
import plotly as py
import plotly.graph_objs as go
from plotly import tools

from articles import articles
from visualisation.plotly_webgl_scatter import plot_scatter


def get_scatter_from_file(file_path, num_clusters, cluster_names, articles):
    full_path = 'data/results/{0}'.format(file_path)
    df = pd.DataFrame.from_csv(full_path)

    # add title and date
    titles = articles_df.loc[df['id'].tolist()]['webTitle']
    df['title'] = titles.tolist()

    dates = articles_df.loc[df['id'].tolist()]['webPublicationDate']
    df['date'] = dates.tolist()

    # add label into
    df['label'] = df['title'] + '\n' + df['date']

    clusters = df.groupby(by='cluster')
    traces = []
    for index, cluster in clusters:
        cluster_name = (cluster_names[index] if len(cluster_names) > index
                        else '')

        trace = plot_scatter(
            cluster['x'], cluster['y'], cluster['label'],
            cluster_name, index
        )
        traces.append(trace)

    return traces


def plot_single_plot(data, result):
    num_clusters = result['num_clusters']
    file_name = 'clusterisation-{0}.html'.format(num_clusters)

    # load results
    full_path = 'data/results/{0}'.format(result['results-file'] + '.csv')
    results_file_df = pd.DataFrame.from_csv(full_path)
    silhoutte_score = results_file_df.iloc[0][0]

    title = 'Clusterisation: {0}, silhoutte_score: {1}'.format(num_clusters,
                                                               silhoutte_score)

    layout = go.Layout(title=title, showlegend=True)
    figure = go.Figure(data=data, layout=layout)

    py.offline.plot(figure, filename='data/' + file_name)
    # py.plotly.iplot(figure, filename=file_name)


def create_figures(data, results):
    NUM_COLS = 2
    num_rows = math.ceil(len(data) / NUM_COLS)

    # get title for all charts
    titles = [
        'Num clusters: {0}'.format(result['num_clusters'])
        for result in results
    ]

    fig = tools.make_subplots(rows=num_rows,
                              cols=NUM_COLS,
                              subplot_titles=titles)

    index = 0
    for datum in data:
        col_index = (index % NUM_COLS) + 1
        row_index = math.floor(index / NUM_COLS) + 1
        fig.append_trace(datum, row_index, col_index)
        index += 1

    return fig


# setup plotly
username = os.environ['PLOTLY_USERNAME']
api = os.environ['PLOTLY_API']
py.tools.set_credentials_file(username=username, api_key=api)

# get documents
documents = articles.get_articles()
article_docs = [document for document in documents]
articles_df = pd.DataFrame(article_docs)
articles_df = articles_df.set_index('id')


results = [
    {
        'results-file': '2017-06-25-22-39-54-519030-clusterisation-results',
        'clusters-file': '2017-06-25-22-40-02-094440-article-clusters',
        'num_clusters': 2,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-25-22-54-20-811355-clusterisation-results',
        'clusters-file': '2017-06-25-22-54-28-487296-article-clusters',
        'num_clusters': 3,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-25-23-08-54-332122-clusterisation-results',
        'clusters-file': '2017-06-25-23-09-01-870842-article-clusters',
        'num_clusters': 4,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-25-23-23-28-956303-clusterisation-results',
        'clusters-file': '2017-06-25-23-23-36-502129-article-clusters',
        'num_clusters': 5,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-25-23-38-02-690425-clusterisation-results',
        'clusters-file': '2017-06-25-23-38-10-227272-article-clusters',
        'num_clusters': 6,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-25-23-52-42-988683-clusterisation-results',
        'clusters-file': '2017-06-25-23-52-50-526944-article-clusters',
        'num_clusters': 7,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-26-00-07-22-595489-clusterisation-results',
        'clusters-file': '2017-06-26-00-07-30-084332-article-clusters',
        'num_clusters': 8,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-26-00-22-02-964196-clusterisation-results',
        'clusters-file': '2017-06-26-00-22-10-504381-article-clusters',
        'num_clusters': 9,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-26-00-36-48-983930-clusterisation-results',
        'clusters-file': '2017-06-26-00-36-56-588418-article-clusters',
        'num_clusters': 10,
        'cluster_names': [
            '2000s', 'Israel/Palestine', '2000s', 'Isis',
            'Muslim Brotherhood (1)', 'War On Terror/Iraq',
            'Bataclan Theatre (1)', 'Middle East', 'Abu Hamza (3)',
            'Northern Ireland'
        ],
    },
    {
        'results-file': '2017-06-26-00-51-33-555914-clusterisation-results',
        'clusters-file': '2017-06-26-00-51-41-082246-article-clusters',
        'num_clusters': 11,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-26-01-06-21-489753-clusterisation-results',
        'clusters-file': '2017-06-26-01-06-28-258814-article-clusters',
        'num_clusters': 12,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-26-01-21-12-912187-clusterisation-results',
        'clusters-file': '2017-06-26-01-21-20-375514-article-clusters',
        'num_clusters': 13,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-26-01-36-04-262736-clusterisation-results',
        'clusters-file': '2017-06-26-01-36-10-935432-article-clusters',
        'num_clusters': 14,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-26-15-00-03-913880-clusterisation-results',
        'clusters-file': '2017-06-26-15-00-11-500040-article-clusters',
        'num_clusters': 15,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-26-15-14-58-993143-clusterisation-results',
        'clusters-file': '2017-06-26-15-15-06-468618-article-clusters',
        'num_clusters': 16,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-26-15-30-04-178275-clusterisation-results',
        'clusters-file': '2017-06-26-15-30-11-567695-article-clusters',
        'num_clusters': 17,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-26-15-45-14-789234-clusterisation-results',
        'clusters-file': '2017-06-26-15-45-22-194345-article-clusters',
        'num_clusters': 18,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-26-16-00-18-744097-clusterisation-results',
        'clusters-file': '2017-06-26-16-00-26-166949-article-clusters',
        'num_clusters': 19,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-26-16-15-23-785523-clusterisation-results',
        'clusters-file': '2017-06-26-16-15-31-157905-article-clusters',
        'num_clusters': 20,
        'cluster_names': []
    },
    {
        'results-file': '2017-06-26-16-31-12-144708-clusterisation-results',
        'clusters-file': '2017-06-26-16-31-19-558506-article-clusters',
        'num_clusters': 21,
        'cluster_names': []
    }
]

# results = [results[8]]


data = [
    get_scatter_from_file(
        result['clusters-file'] + '.csv', result['num_clusters'],
        result['cluster_names'], articles_df
    )
    for result in results
]


for i, datum in enumerate(data):
    result = results[i]
    plot_single_plot(datum, result)


# fig = create_figures(data, results)
# fig['layout'].update(autosize=True, title='Clusterisation')
# py.offline.plot(fig, filename='make-subplots-multiple-with-titles.html')
