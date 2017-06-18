from sklearn.feature_extraction.text import TfidfVectorizer

from caching import caching

CACHE_OPERATION_KEY = 'tf-idf'


def fit_texts(texts, tokenizer, ngram_range=(1, 3), stop_words='english',
              cache_params={}):

    cache_params['operation'] = CACHE_OPERATION_KEY
    cache_params['ngram_range'] = ngram_range
    cache_params['stop_words'] = stop_words

    # do we have cached model?
    cached_model = caching.get_results(cache_params)
    if cached_model:
        print('TF-IDF using cached model')
        return cached_model

    print('TF-IDF computing model')

    vectorizer = TfidfVectorizer(
        stop_words=stop_words,
        use_idf=True,
        tokenizer=tokenizer,
        ngram_range=ngram_range
    )

    matrix = vectorizer.fit_transform(texts)

    # cache result
    result = (vectorizer, matrix)
    caching.store_result(cache_params, result)

    return result
