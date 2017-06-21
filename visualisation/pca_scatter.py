from PIL import Image

# https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python
import matplotlib as mpl
mpl.use('TkAgg')

import matplotlib.pyplot as plt


PCA_SCATTER_FILE_PATH = 'data/svg_scatter.png'


def save_plot(plt, image_path=PCA_SCATTER_FILE_PATH):
    plt.savefig(image_path)
    Image.open(image_path).save(image_path, 'png')


def plot_scatter(df, image_path=PCA_SCATTER_FILE_PATH):
    # group by cluster
    groups = df.groupby(by='cluster')
    clusters = df['cluster']

    # set up plot
    fig, ax = plt.subplots(figsize=(200, 100))

    for name, group in groups:
        ax.plot(group.x, group.y, label=clusters, marker='o', ms=12,
                linestyle='')
        ax.set_aspect('auto')
        ax.tick_params(
          axis='x',         # changes apply to the x-axis
          which='both',      # both major and minor ticks are affected
          bottom='off',      # ticks along the bottom edge are off
          top='off',         # ticks along the top edge are off
          labelbottom='off')
        ax.tick_params(
          axis='y',         # changes apply to the y-axis
          which='both',      # both major and minor ticks are affected
          left='off',        # ticks along the bottom edge are off
          top='off',         # ticks along the top edge are off
          labelleft='off')

    # add label in x,y position with the label as the film title
    for i in range(len(df)):
        ax.text(df.ix[i]['x'], df.ix[i]['y'], df.ix[i]['webTitle'], size=8)

    # ax.legend(numpoints=1)
    save_plot(plt, image_path)
