from tokenizer import tokenizer
from tokenizer.remove_html import remove_html
from tokenizer.stem_words import stem_words
from tokenizer.remove_punctuation import remove_punctuation


def tokenize_and_stem(text):
    # tokenize
    tokens = tokenizer.tokenize(text)

    # remove punctuation
    tokens = remove_punctuation(tokens)

    # stem
    tokens = stem_words(tokens)

    # to lowercase
    return tokens
