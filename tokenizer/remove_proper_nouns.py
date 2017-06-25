import string

import nltk

# interested in singular and plural proper nouns
# http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
PROPER_NOUNS_TAGS = ['NNP', 'NNPS']


def remove_lowercase_noun(tokens):
    tokens = [word for word in tokens if word.islower()]
    return tokens


def filter_proper_nouns(tag):
    return tag not in PROPER_NOUNS_TAGS


def remove_proper_nouns(tokens):
    tags = nltk.pos_tag(tokens)
    filtered_tokens = [tag[0] for tag in tags if filter_proper_nouns(tag[1])]

    # debug - see removed words
    # propers = [tag[0] for tag in tags if tag[1] == 'NNP']

    return filtered_tokens
