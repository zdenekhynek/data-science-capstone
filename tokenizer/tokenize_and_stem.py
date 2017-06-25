from tokenizer import tokenizer
from tokenizer.remove_html import remove_html
from tokenizer.stem_words import stem_words
from tokenizer.remove_punctuation import remove_punctuation
from tokenizer.remove_proper_nouns import remove_lowercase_noun


def tokenize_and_stem(text):
    # tokenize
    tokens = tokenizer.tokenize(text)

    # remove punctuation
    tokens = remove_punctuation(tokens)

    # remove propers
    tokens = remove_lowercase_noun(tokens)

    # stem
    tokens = stem_words(tokens)

    # to lowercase
    return tokens
