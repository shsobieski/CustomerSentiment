def predict_sentiment(model):
    data = input(str('Enter a test tweet...'))
    cleaned_data = clean_lemmatize_token(data)
    next_step = [cleaned_data, '']
    vect_data = tf_idfvectorizer.transform(next_step)
    model = XGBClassifier(scale_pos_weight=.96, learning_rate = 0.1, 
                          max_depth = 3, n_estimators = 180)
    model.fit(X_train_SMOTE, y_train_SMOTE)
    pred = model.predict(vect_data)
    return pred