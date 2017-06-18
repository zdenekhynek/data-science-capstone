from PIL import Image

# https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python
import matplotlib as mpl
mpl.use('TkAgg')

import matplotlib.pyplot as plt


default_image_path = 'data/svg_scatter.png'

def save_plot(plt, image_path = default_image_path):
  plt.savefig(image_path)
  Image.open(image_path).save(image_path,'png')


def plot_scatter(df, image_path = default_image_path):
  # group by cluster
  groups = df.groupby(by='cluster')

  # set up plot
  fig, ax = plt.subplots(figsize=(17, 9)) # set size
  ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling

  # iterate through groups to layer the plot
  # note that I use the cluster_name and cluster_color dicts with the 'name' lookup to return the appropriate color/label
  for name, group in groups:
      ax.plot(group.x, group.y, marker='o', linestyle='', ms=12,
              label=clusters, mec='none')
      ax.set_aspect('auto')
      ax.tick_params(\
          axis= 'x',         # changes apply to the x-axis
          which='both',      # both major and minor ticks are affected
          bottom='off',      # ticks along the bottom edge are off
          top='off',         # ticks along the top edge are off
          labelbottom='off')
      ax.tick_params(\
          axis= 'y',         # changes apply to the y-axis
          which='both',      # both major and minor ticks are affected
          left='off',        # ticks along the bottom edge are off
          top='off',         # ticks along the top edge are off
          labelleft='off')

  # add label in x,y position with the label as the film title
  for i in range(len(df)):
      ax.text(df.ix[i]['x'], df.ix[i]['y'], df.ix[i]['webTitle'], size=8)

  #plt.show() #show the plot

  save_plot(plt, image_path)
