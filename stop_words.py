from nltk.corpus import stopwords

english_stops = stopwords.words('english')


def filter_stop_words(words, stops=english_stops):
    filtered_words = [word for word in words if word not in stops]
    return filtered_words
