from gensim import corpora, models


def create_dictionary(texts):
    return corpora.Dictionary(texts)


def create_corpus(dictionary, texts):
    return [dictionary.doc2bow(text) for text in texts]


def fit_model(texts, params):

    # create a Gensim dictionary from the texts
    dictionary = create_dictionary(texts)

    # remove extremes (similar to the min/max df step used when creating
    # the tf-idf matrix)
    dictionary.filter_extremes(params['no_below'], params['no_above'])

    # convert the dictionary to a bag of words corpus for reference
    corpus = create_corpus(dictionary, texts)

    lda = models.LdaModel(corpus,
                          num_topics=params['num_topics'],
                          id2word=dictionary,
                          update_every=params['update_every'],
                          chunksize=params['chunksize'],
                          passes=params['passes'])

    return lda
