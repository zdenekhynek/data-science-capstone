from .text_visualisation import store_results

DEFAULT_LDA_TOPIC_FILE_PATH = 'data/lda_topics.txt'


def print_lda_topics(lda, result_file = DEFAULT_LDA_TOPIC_FILE_PATH):
  result = ''

  topics = lda.show_topics()[0]
  result = ''.join(map(str, topics))
  store_results(result, result_file)
