import os

import pandas as pd
import plotly as py
import plotly.graph_objs as go
import numpy as np
import colorlover as cl


def plot_scatter(x, y, color, title):
    trace = go.Scattergl(
      x=x,
      y=y,
      mode='markers',
      marker=dict(
          color=color,
          line=dict(
              width=1,
              color=color
          )
      ),
      text=title
    )

    return trace