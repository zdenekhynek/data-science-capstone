import os
import math

import pandas as pd
import plotly as py
import plotly.graph_objs as go
import numpy as np
import colorlover as cl
from plotly import tools

from articles import articles
from visualisation.plotly_webgl_scatter import plot_scatter


def get_scatter_from_file(file_path, num_clusters, articles):
    full_path = 'data/results/{0}'.format(file_path)
    df = pd.DataFrame.from_csv(full_path)

    # add title and date
    titles = articles_df.loc[df['id'].tolist()]['webTitle']
    df['title'] = titles.tolist()

    dates = articles_df.loc[df['id'].tolist()]['webPublicationDate']
    df['date'] = dates.tolist()

    # add label into
    df['label'] = df['title'] + ',' + df['date']

    # add colors (if only 2, use minimum, which is 3)
    if num_clusters < 3:
        num_clusters = 3
    color_scale = cl.scales[str(num_clusters)]['qual']['Paired']

    colors = [color_scale[cluster_index] for cluster_index in df['cluster']]
    trace = plot_scatter(df['x'], df['y'], colors, df['label'])

    return trace


def create_figures(data):
    NUM_COLS = 2
    num_rows = math.ceil(len(data) / NUM_COLS)

    fig = tools.make_subplots(rows=num_rows,
                              cols=NUM_COLS)

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
        'file': '2017-06-24-21-10-16-463237-article-clusters.csv',
        'num_clusters': 12
    },
    {
        'file': '2017-06-24-09-51-12-895317-article-clusters.csv',
        'num_clusters': 12
    }
]

data = [
    get_scatter_from_file(result['file'], result['num_clusters'], articles_df)
    for result in results
]


fig = create_figures(data)
fig['layout'].update(height=1200, width=1200, title='Multiple Subplots' +
                                                    ' with Titles')

py.offline.plot(fig, filename='make-subplots-multiple-with-titles.html')
