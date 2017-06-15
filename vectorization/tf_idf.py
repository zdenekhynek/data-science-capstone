from sklearn.feature_extraction.text import TfidfVectorizer


def fit_texts(texts, tokenizer, ngram_range=(1,3), stop_words='english'):
  vectorizer = TfidfVectorizer(
    stop_words=stop_words,
    use_idf=True,
    tokenizer=tokenizer,
    ngram_range=ngram_range
  )

  matrix = vectorizer.fit_transform(texts)
  return vectorizer, matrix
