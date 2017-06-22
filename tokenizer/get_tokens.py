import pandas as pd
from collections import Counter

from tokenizer.tokenize_and_stem import tokenize_and_stem
from tokenizer.stop_words import filter_stop_words


def get_filtered_tokens(texts):
    tokens = [token for text in texts for token in tokenize_and_stem(text)]
    return filter_stop_words(tokens)


def get_tokens_count(tokens):
    data = Counter(tokens).most_common()
    return pd.DataFrame(data)


def get_texts_tokens(texts):
    filtered_tokens = get_filtered_tokens(texts)
    return get_tokens_count(filtered_tokens)


def most_common_tokens(texts):
    return get_texts_tokens(texts).most_common(10)
