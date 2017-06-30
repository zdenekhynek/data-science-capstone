from sklearn.feature_extraction.text import TfidfVectorizer

CACHE_OPERATION_KEY = 'tf-idf'


def fit_texts(texts, tokenizer, params={}):
    # params = cache_params.copy()
    # params['operation'] = CACHE_OPERATION_KEY
    # params['ngram_range'] = ngram_range
    # params['stop_words'] = stop_words

    # do we have cached model?
    # cached_model = caching.get_results(params)
    # if cached_model:
    #    print('TF-IDF using cached model')
    #    return cached_model

    # print('TF-IDF computing model')

    vectorizer = TfidfVectorizer(
        stop_words='english',
        use_idf=True,
        tokenizer=tokenizer,
        ngram_range=params['ngram_range'],
        min_df=params['min_df'],
        max_df=params['max_df'],
        max_features=params['max_features']
    )

    matrix = vectorizer.fit_transform(texts)

    # cache result
    result = (vectorizer, matrix)
    # caching.store_result(params, result)

    return result
