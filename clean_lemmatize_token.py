def clean_lemmatize_token(tweet):
    """Function used to automatically remove stop words, twitter_specific words and punctuation, tokenize, lemmatize
    and join together words into one string before modeling"""
    stop_words = set(stopwords.words('english'))
    cleaned = tweet.translate(str.maketrans('', '', string.punctuation)).lower()
    tokenized = word_tokenize(cleaned)
    filtered = [w for w in tokenized if not w in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized = []
    for word in filtered:
        lemmatized.append(lemmatizer.lemmatize(word))
    to_remove = ['rt','mention','sxsw','link']
    lemmatized = [w for w in lemmatized if w not in to_remove]
    lemmatized = ' '.join(lemmatized)
    return lemmatized
