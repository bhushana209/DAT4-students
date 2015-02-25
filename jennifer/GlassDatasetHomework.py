# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 10:28:34 2015

@author: jen_lambert13
"""


# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split


# read in data file from url
pd.read_table("http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data")
glass = pd.read_table("http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data", sep=',')

glass.head(10)

#name the columns in the data set
g_cols = ['id_number', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Glass_Type']
glass = pd.read_table('http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data', header=None, sep=',', names=g_cols, index_col='id_number')

#convert into a dataframe
glass = pd.DataFrame(glass, columns=g_cols)
glass.isnull().sum()   # no automatic handling of missing values
glass.dtypes           # type is 'object' because list elements were strings

#create a new column 'binary'
# add a new column as a function of existing columns

np.where(glass.Glass_Type<5, 0,1)
glass['binary']=np.where(glass.Glass_Type<5, 0,1)

#Create X using all features and create y using binary
feature_cols = ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']
X = glass[feature_cols]
y = glass.binary

#Train, test, split - split X and y into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)
X_train.shape
X_test.shape
y_train.shape
y_test.shape

#Fit a logistic regression model on the training set
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

#Make predictions on test set
preds = logreg.predict(X_test)
from sklearn import metrics
print metrics.accuracy_score(y_test, preds)

#Print confusion matrix
print metrics.confusion_matrix(y_test, preds)

#Calculate accuracy and compare it to the null accuracy rate
print metrics.accuracy_score(y_test, preds)
y_test.mean()
1 - y_test.mean()

#Calculate the AUC
probs = logreg.predict_proba(X_test)[:, 1]
print metrics.roc_auc_score(y_test, probs)

#Use cross-validation (with AUC as the scoring metric) to compare three models: 1) logistic regression; 2) KNN (K=1); and 3) KNN (K=3)
from sklearn.cross_validation import cross_val_score
logreg = LogisticRegression()
cross_val_score(logreg, X, y, cv=10, scoring='roc_auc').mean()

knn = KNeighborsClassifier(n_neighbors=1)
scores = cross_val_score(knn, X, y, cv=5, scoring='roc_auc')
scores
np.mean(scores)

knn = KNeighborsClassifier(n_neighbors=3)
scores = cross_val_score(knn, X, y, cv=5, scoring='roc_auc')
scores
np.mean(scores)

