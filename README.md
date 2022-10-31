# Credit Card Transaction Fraud Detection

##### badges

An end-to-end Machine Learning Project to detect fraud in credit card transactions.

## Problem Statement

With the growth of e-commerce websites, people and financial companies rely on online services to carry out their transactions that have led to an exponential increase in the credit card frauds. Fraudulent credit card transactions lead to a loss of huge amount of money. The design of an effective fraud detection system is necessary in order to reduce the losses incurred by the customers and financial companies.

Therefore, in this project we develop a Streamlit App that utilizes a Machine Learning model(XGBoost) as an API to detect potential fraud in credit card transactions, based on the following criteria: Type of transaction, Amount(money), Old balance orig, New balance orig, Old balance dest, New balance dest.

The App can be viewed through this [link]()

[NoteBook]()

## Data Preparation

Credit card transaction is a syntetic financial dataset created using a simulator called PaySim. In this sense, PaySim uses aggregated data from the private dataset to generate a synthetic dataset that resembles the normal operation of transactions and injects malicious behaviour to later evaluate the performance of fraud detection methods.

#### Data preprocessing stets:
 - Clean the data: removed duplicate values, missing values, unnecessary and leakage variables
 - Transform no-numerical variables to numerical variables
 - Split the data into train, validation and test sets

Source dataset: [Credit card data](https://www.kaggle.com/datasets/ealaxi/paysim1)

## Modelling 
Machine Learning Algorithms that were tested:
 - Random Forest 
 - LightGBM
 - XGBoost

Xgboost was the model with better performance with the validation set:
 - Accuracy: 0.93
 - F1-Score: 0.90
 - ROC-AUC: 0.93
 
Xgboost was chosen like the final model and its hyperparameters were optimized using hyperopt(library) with a Bayesian optimization like search strategy.

Xgboost was the model with better performance with the test set:
 - Accuracy: 0.99
 - F1-Score: 0.89
 - ROC-AUC: 0.91
 
 Feature importance
 ![image](https://github.com/Luissalazarsalinas/Fraud-Detection/blob/master/img/Feature_importance.png)
The variables that contribute most to the XGBoost final model were:
 - Type of transferent
 - New balance orig
 - Old balance orig
These variables could be good predictors to detect fraud in credit card transactions.

## Deploy
