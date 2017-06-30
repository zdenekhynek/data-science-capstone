import plotly.graph_objs as go


def plot_scatter(x, y, title, name, color):
    trace = go.Scattergl(
      x=x,
      y=y,
      mode='markers',
      name=name,  # for legend
      marker=dict(
          color=color,
          line=dict(
              width=0.2,
              color=color
          ),
          colorscale='Viridis'
      ),
      text=title
    )

    return trace
