from nltk.stem.snowball import SnowballStemmer

english_snowball_stemmer = SnowballStemmer('english')

def stem_words(words, stemmer=english_snowball_stemmer):
    stems = [stemmer.stem(t) for t in words]
    return stems
