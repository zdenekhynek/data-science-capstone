import pandas as pd


def get_weighted_tokens(vectorizer):
    tokens = dict(zip(vectorizer.get_feature_names(), vectorizer.idf_))
    df = pd.DataFrame(columns=['tfidf']).from_dict(tokens, orient='index')
    df.columns = ['tfidf']
    return df.sort_values(by=['tfidf'], ascending=False)


def most_important_tokens(vectorizer):
    df = get_weighted_tokens(vectorizer)
    return df.head(30)
