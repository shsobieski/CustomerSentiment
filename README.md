# Customer Sentiment Analysis

### Objective
The objective of this project is to predict the sentiment of tweets that reference specific products. This information has applications in R&D and marketing for technology and communications businesses.

### The Data
The dataset utilized for this model is a set of 9092 tweets collected during the SXSW festival. The data was labeled by humans as having either positive, negative, or neutral sentiment toward a product. Products in the dataset included Apple, Google and Android products and services. Data was obtained through data.world and is availble to import through the link below. 

https://query.data.world/s/zbehvjkmiewbkln44rae6iphum4v3g

![](http://localhost:8890/view/figures/SentimentbyProduct.png "Sentiment by Product/Brand")

### The Model
For this project two models were made: one being a binary classifier identifying either positive or negative sentiment. The other being a multiclass classifier identifying either positive, negative, or neutral sentiment.

The binary classifier used was XGBoosted Random Forest Classifier trained on SMOTE data . The model scored an recall score of 90% and a recal score of 90% in identifying negative sentiment. The model scored an accuracy score of 90% and a recall score of 90% in identifying positive sentiment. 



The multiclass classifier used was ** . The model scored an accuracy score of ** and a recal score of ** in identifying negative sentiment. The model scored an accuracy score of ** and a recall score of ** in identifying positive sentiment. For identifying neutral sentiment the model scored an accuracy score of ** and a recall score of ** . 

### Analysis
Using the most predictive model, we discovered particular phrases to appear most frequently in negative tweets versus positive tweets. 

### Reccomendation
Our reccomendation for use of this model is to 
