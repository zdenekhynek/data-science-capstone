from articles import articles
from tokenizer.tokenize_and_stem import tokenize_and_stem
from tokenizer.stop_words import filter_stop_words
from tokenizer.remove_html import remove_html
from topics import lda
from results import results
from performance.benchmarks import Benchmarks


def run_pipeline(parameters={}):
    benchmarks = Benchmarks()

    doc_params = parameters['documents']
    documents = articles.get_articles(doc_params['query']).limit(doc_params['limit'])
    article_docs = [document for document in documents]
    texts = articles.get_document_texts(article_docs)
    benchmarks.add_benchmark('1-get-articles')

    # remove html
    texts = [remove_html(text) for text in texts]
    benchmarks.add_benchmark('2-remove-html')

    # tokenize
    tokenized_texts = [tokenize_and_stem(text) for text in texts]
    benchmarks.add_benchmark('3-tokenize')

    # remove stop word
    tokens = [filter_stop_words(text) for text in tokenized_texts]
    benchmarks.add_benchmark('4-filter-stop-words')
    results.store_lda_tokens(parameters, tokens)

    # fit lda
    fitted_lda = lda.fit_model(tokens, parameters['lda'])
    benchmarks.add_benchmark('5-fitting-model')
    results.store_lda(parameters, fitted_lda)

    # show lda topics
    topics = fitted_lda.show_topics(formatted=True)
    results.store_lda_topics(parameters, topics)
    benchmarks.add_benchmark('6-storing-results')

    results.store_performance(parameters, benchmarks.get_benchmarks())


news_only_query = {'$or': [{'sectionId': 'world'}, {'sectionId': 'uk-news'}]}


parameters = {
    'documents': {
        'query': news_only_query,
        'limit': 2
    },
    'lda': {
        'num_topics': 20,
        'no_below': 1,
        'no_above': 0.8,
        'update_every': 5,
        'chunksize': 10000,
        'passes': 100
    }
}

# run_pipeline(parameters)


def run_lda_year(year_tuple):
    date_query = {
        'webPublicationDate': {'$gte': year_tuple[0], '$lt': year_tuple[1]}
    }
    parameters['documents']['query'] = {'$and': [news_only_query, date_query]}
    run_pipeline(parameters)


def run_lda_years_range(years):
    for year in years:
        run_lda_year(year)


years = [
    ('1900', '1990'),
    ('1990', '2000'),
    ('2000', '2001'),
    ('2001', '2002'),
    ('2002', '2003'),
    ('2003', '2004'),
    ('2004', '2005'),
    ('2005', '2006'),
    ('2006', '2007'),
    ('2007', '2008'),
    ('2008', '2009'),
    ('2009', '2010'),
    ('2010', '2011'),
    ('2011', '2012'),
    ('2012', '2013'),
    ('2013', '2014'),
    ('2014', '2015'),
    ('2015', '2016'),
    ('2016', '2017'),
    ('2017', '2018')
]

run_lda_years_range(years)
