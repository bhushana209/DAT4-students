# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 16:39:51 2015
Kerry Jones
Feb 1 ,2015
Model_eval HW
@author: MindKontrol
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
col = ["id_number", "ri", "na","mg","al","si", "k", "ca", "ba", "fe", "type"]
data = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data',names = col )


data.describe()
data.groupby('type').describe()
data.columns
data.dtypes #mixture of data types(integers, floats,string objects )
data.shape # There are currently 18801 rows and 33 columns
data.values #dataframe as array
data.info() 
data.type.hist(bins = 10)


data['binary'] = 0 # create new varible, set values to 0
one = data.type >  4 # if type is greater than 4 then binary becomes one.
data.loc[one, 'binary'] = 1


#Part 2 
feature_cols = ["ri", "na","mg","al","si", "k", "ca", "ba", "fe"] 
X = data[feature_cols]
y = data['binary']
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4)
X_train
X_test
y_test
y_train
train = pd.DataFrame(data=X_train, columns=["ri", "na","mg","al","si", "k", "ca", "ba", "fe"])




#==============================================================================
# train.plot(x='ri', y='na', kind='scatter', alpha=0.3)
# train.plot(x='ri', y='mg', kind='scatter', alpha=0.3)
# train.plot(x='ri', y='al', kind='scatter', alpha=0.3)
# train.plot(x='ri', y='si', kind='scatter', alpha=0.3)
# train.plot(x='ri', y='k', kind='scatter', alpha=0.3)
# train.plot(x='ri', y='ca', kind='scatter', alpha=0.3)
# train.plot(x='ri', y='ba', kind='scatter', alpha=0.3)
# train.plot(x='ri', y='fe', kind='scatter', alpha=0.3)
# 
# plt.ylim([0,80000]); plt.xlim([0, 2800])
#==============================================================================
#Part 3

from sklearn.linear_model import LogisticRegression

logRe= LogisticRegression()
logRe.fit(train[["ri", "na","mg","al","si", "k", "ca", "ba", "fe"]], y_train)
B1 = logRe.coef_[0][0] 
B0 = logRe.intercept_[0]
np.exp(B1)  #.9881, less than 1 so it is not significant. 

#Predict
preds = logRe.predict(X_test)
preds

from sklearn import metrics

print metrics.confusion_matrix(y_test, preds) # Confusion table

#accuracy 
print metrics.accuracy_score(y_test, preds)

# compare to null accuracy rate
y_test.mean()
1 - y_test.mean()

#Predict probability 
probs = logRe.predict_proba(X_test)[:, 1]
#plt.hist(probs)

#Calculate AUC 
print metrics.roc_auc_score(y_test, probs)



#part 4
#USe cross validation with AUC metric from sklearn.cross_validation import cross_val_score to compare models
#Part 4
cross_val_score(logRe, X, y, cv=10, scoring='roc_auc').mean()

from sklearn.neighbors import KNeighborsClassifier  # import class

knn = KNeighborsClassifier(n_neighbors=1)           # instantiate the estimator(create an instance of )

knn5 = KNeighborsClassifier(n_neighbors=5)           # instantiate the estimator(create an instance of )


cross_val_score(knn, X, y, cv=10, scoring='roc_auc').mean()

cross_val_score(knn5, X, y, cv=10, scoring='roc_auc').mean()


