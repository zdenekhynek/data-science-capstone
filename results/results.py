from os import path
from datetime import datetime

import pandas as pd

from database import DB_NAME, RESULTS_COLLECTION_NAME
from database.client import client

RESULTS_FOLDER = 'data/results'


def get_collection(db_name=DB_NAME, collection_name=RESULTS_COLLECTION_NAME):
    db = client[db_name]
    collection = db[collection_name]
    return collection


def get_current_date():
    # returns string in format
    # YYYY-MM-DD-HH-MM-SS-mmmmm
    return datetime.today().strftime('%Y-%m-%d-%H-%M-%S-%f')


def get_file_name(operation, extension='csv'):
    date = get_current_date()
    return '{0}-{1}.{2}'.format(date, operation, extension)


def get_file_full_path(file_name, folder=RESULTS_FOLDER):
    return path.join(folder, file_name)


# def store_csv_data(file_path, data):
    # convert data to panda dataframe
    # (expects either list-like or dictionary-like data types)
#   df = pd.DataFrame(data)

    # store into csv
#    df.to_csv(file_path)


def store_result_record(params={}, operation='', file=''):
    collection = get_collection()
    record = collection.find_one(params)

    if record is None:
        record = {}
        record['params'] = params

    record['{0}-file'.format(operation)] = file
    collection.save(record)


def store_tokens(params={}, tokens_df=pd.DataFrame()):
    operation = 'tokens'
    file_name = get_file_name(operation, 'csv')
    full_path = get_file_full_path(file_name)

    # dump results into a file
    tokens_df.to_csv(full_path)

    # store record about run into databse
    store_result_record(params, operation, full_path)


def store_idf_tokens(params={}, tokens_df=pd.DataFrame()):
    operation = 'tokens-idf'
    file_name = get_file_name(operation, 'csv')
    full_path = get_file_full_path(file_name)

    # dump results into a file
    tokens_df.to_csv(full_path)

    # store record about run into databse
    store_result_record(params, operation, full_path)


def store_cluster_tokes(params={}, clusters_tokens=[]):
    operation = 'clusters-tokens'
    file_name = get_file_name(operation, 'csv')
    full_path = get_file_full_path(file_name)

    # select columns we're interested in
    df = pd.DataFrame(clusters_tokens)

    # we want cluster ids as columns and tokens in rows
    # will have much less columns then rows
    df = df.transpose()

    # dump results into a file
    df.to_csv(full_path)

    # store record about run into databse
    store_result_record(params, operation, full_path)


def store_cluster_articles(params={}, articles_df=pd.DataFrame()):
    operation = 'article-clusters'
    file_name = get_file_name(operation, 'csv')
    full_path = get_file_full_path(file_name)

    # select columns we're interested in
    df = articles_df[['id', 'cluster', 'x', 'y']]

    # dump results into a file
    df.to_csv(full_path)

    # store record about run into databse
    store_result_record(params, operation, full_path)


def store_clusterisation_results(params={}, silhouette_score=0):
    operation = 'clusterisation-results'
    file_name = get_file_name(operation, 'csv')
    full_path = get_file_full_path(file_name)

    # select columns we're interested in
    results = {'silhouette_score': silhouette_score}
    df = pd.DataFrame.from_dict(results, orient='index')

    # dump results into a file
    df.to_csv(full_path)

    # store record about run into databse
    store_result_record(params, operation, full_path)


def store_performance(params={}, benchmarks=[]):
    operation = 'benchmarks'
    file_name = get_file_name(operation, 'csv')
    full_path = get_file_full_path(file_name)

    # conver list to pandas
    df = pd.DataFrame(benchmarks)

    # dump results into a file
    df.to_csv(full_path)

    # store record about run into databse
    store_result_record(params, operation, full_path)


def store_lda():
    pass
