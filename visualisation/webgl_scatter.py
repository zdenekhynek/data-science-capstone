import os

import pandas as pd
import plotly as py
import plotly.graph_objs as go

import numpy as np

username = os.environ['PLOTLY_USERNAME']
api = os.environ['PLOTLY_API']

py.tools.set_credentials_file(username=username, api_key=api)


def plot_scatter(x, y, cluster, title):
    trace = go.Scattergl(
      x=x,
      y=y,
      mode='markers',
      marker=dict(
          color=cluster,
          line=dict(
              width=1,
              color=cluster)
      ),
      text=title
    )
    data = [trace]
    py.plotly.iplot(data, filename='WebGL100000')


# file_path = '2017-06-24-11-48-07-165682-article-clusters.csv'
# file_path = '2017-06-24-11-48-07-165682-article-clusters.csv'
# file_path = '2017-06-24-09-51-12-895317-article-clusters.csv'
file_path = '2017-06-24-21-10-16-463237-article-clusters.csv'

full_path = 'data/results/{0}'.format(file_path)
df = pd.DataFrame.from_csv(full_path)
plot_scatter(df['x'], df['y'], df['cluster'], df['id'])
