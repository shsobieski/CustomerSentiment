# Customer Sentiment Analysis

### Objective
The objective of this project is to predict the sentiment of tweets that reference specific products. This information has applications in R&D and marketing for technology and communications businesses.

### The Data
The dataset utilized for this model is a set of 9092 tweets collected during the SXSW festival. The data was labeled by humans as having either positive, negative, or neutral sentiment toward a product. Products in the dataset included Apple, Google and Android products and services. Data was obtained through data.world and is availble to import through the link below. 

https://query.data.world/s/zbehvjkmiewbkln44rae6iphum4v3g

<img src='/figures/SentimentbyProduct.png' />

### The Model
For this project two models were made: one being a binary classifier identifying either positive or negative sentiment. The other being a multiclass classifier identifying either positive, negative, or neutral sentiment.

The binary classifier used was XGBoosted Random Forest Classifier trained on SMOTE data . The model scored an F-1 score of 90% and a recall score of 90% in identifying negative sentiment. The model scored a F-1 score of 90% and a recall score of 90% in identifying positive sentiment. 

<img src='/figures/binarymodelresults.png' />

The multiclass classifier used was also the XGBoosted Random Forest Classifier trained on the SMOTE Data. While the Multinomial Naive Bayes classifier, was more predictive on the train and test set, the training model was overfit to the point where I would not recommend using this model. 

The model scored a F-1 score of 81 and a recal score of 77 in identifying negative sentiment. The model scored an F-1 score of 57 and a recall score of 49 in identifying positive sentiment. For identifying neutral sentiment the model scored an F-1 score of 69 and a recall score of 82. 

<img src='/figures/multiclassmodelresults.png' />

Complete rundown of all classification models run, binary and multiclass, below. 

<img src='/figures/modelresults.png' />

<img src='/figures/modelresults2.png' />

### Analysis
Using the most predictive model, we discovered particular phrases to appear most frequently in negative tweets versus positive tweets. 

### Reccomendation
Our reccomendation for use of this model is to 
