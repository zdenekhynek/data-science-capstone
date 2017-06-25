from tokenizer import tokenizer
from tokenizer.remove_html import remove_html
from tokenizer.stem_words import stem_words
from tokenizer.remove_punctuation import remove_punctuation
from tokenizer.remove_proper_nouns import remove_proper_nouns


def tokenize_and_stem(text, remove_propes=True):
    # tokenize
    tokens = tokenizer.tokenize(text)

    # remove punctuation
    tokens = remove_punctuation(tokens)

    if remove_propes:
        # remove proper words
        tokens = remove_proper_nouns(tokens)

    # stem
    tokens = stem_words(tokens)

    # to lowercase
    return tokens
