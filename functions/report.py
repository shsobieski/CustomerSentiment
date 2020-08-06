def report(clf):
    """
    Prints the metrics of a classification model
    
    """
    # fit the classifier
    clf.fit(X_train, y_train)
    
    # make predictions
    y_pred = clf.predict(X_test)

    # print accuracy metrics
    report = classification_report(y_test, y_pred)
    print(report)

    fig, ax = plt.subplots(figsize= (8,8))
    plot_confusion_matrix(clf, X_test, y_test, ax=ax)
