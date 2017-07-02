from sklearn.feature_extraction.text import TfidfVectorizer

# key under which the operation result will be stored in the cache collection
CACHE_OPERATION_KEY = 'tf-idf'


def fit_texts(texts, tokenizer, cache_params={}):
    """
    Create tf-idf matrix from the list of texts
    http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
    """

    # construct cache query object to find out if we've run this operation
    # already and might be able to use cached results instead (saves time)
    params = cache_params.copy()
    params['operation'] = CACHE_OPERATION_KEY
    params['ngram_range'] = ngram_range
    params['stop_words'] = stop_words

    # do we have cached model?
    cached_model = caching.get_results(params)
    if cached_model:
        return cached_model

    # we don't have cache model, instatniate k means
    vectorizer = TfidfVectorizer(
        stop_words='english',
        use_idf=True,
        tokenizer=tokenizer,
        ngram_range=params['ngram_range'],
        min_df=params['min_df'],
        max_df=params['max_df'],
        max_features=params['max_features']
    )

    # fit matrix
    matrix = vectorizer.fit_transform(texts)

    # store both vectorizer and matrix so that we can get resuse them later
    # independtly
    result = (vectorizer, matrix)

    # cache result
    caching.store_result(params, result)

    return result
