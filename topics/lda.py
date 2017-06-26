from gensim import corpora, models, similarities

lda = False


def print_topic_words():
    topics_matrix = lda.show_topics(formatted=False, num_words=20)
    topics_matrix = np.array(topics_matrix)

    topic_words = topics_matrix[:, :, 1]
    for i in topic_words:
        print([str(word) for word in i])
        print()


def fit_model(texts, params):
    global lda

    # create a Gensim dictionary from the texts
    dictionary = corpora.Dictionary(texts)

    # remove extremes (similar to the min/max df step used when creating
    # the tf-idf matrix)
    dictionary.filter_extremes(params['no_below'], params['no_above'])

    # convert the dictionary to a bag of words corpus for reference
    corpus = [dictionary.doc2bow(text) for text in texts]

    lda = models.LdaModel(corpus,
                          num_topics=params['num_topics'],
                          id2word=dictionary,
                          update_every=params['update_every'],
                          chunksize=params['chunksize'],
                          passes=params['passes'])

    return lda
