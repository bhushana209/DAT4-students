# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 11:42:16 2015

@author: rdecrescenzo
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import cross_val_score
'''
Part 1
'''
names = "refractive_index", "sodium", "magnesium","aluminum", "silicon", "potassium", "calcium", "barium", "iron", "glass_type"
 
glass = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data", index_col = [0], names=names)
# I used glass and glass.head in the console to check, I also read the background on the data

glass['binary'] = glass.glass_type.map({1:0,2:0,3:0,4:0,5:1,6:1,7:1})
#I used glass and glass.head to check the data


'''
Part 2
'''
glass_features = ["refractive_index", "sodium", "magnesium","aluminum", "silicon", "potassium", "calcium", "barium", "iron"]

X = glass[glass_features]
y = glass.binary

'''
Part 3
'''

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
#checked by looking in console

train = pd.DataFrame(data=X_train, columns=["refractive_index", "sodium", "magnesium","aluminum", "silicon", "potassium", "calcium", "barium", "iron"])
train['default'] = y_train
test = pd.DataFrame(data=X_test, columns=["refractive_index", "sodium", "magnesium","aluminum", "silicon", "potassium", "calcium", "barium", "iron"])
test['default'] = y_test

cls = LogisticRegression()
cls.fit(train, y_train)
predictions = cls.predict(test)
print confusion_matrix(predictions,y_test)

#That's good, but I don't want to overfit. Is there a way to use less variables?

#Let's try the refractive index and aluminum, keeping in mind that the two categories are windows and other

#The window glass is "flat glass" the other glass is "container glass"
#flat glass has higher magnesium oxide and sodium oxide
#container glass has higher silica, calcium oxide, and aluminum oxide 
cls = LogisticRegression()
cls.fit(train[["refractive_index", "aluminum"]], y_train)
predictions = cls.predict(test[["refractive_index", "aluminum"]])
print confusion_matrix(predictions,y_test)

cls = LogisticRegression()
cls.fit(train[["refractive_index", "aluminum","magnesium"]], y_train)
predictions = cls.predict(test[["refractive_index", "aluminum","magnesium"]])
print confusion_matrix(predictions,y_test)

cls = LogisticRegression()
cls.fit(train[["refractive_index", "aluminum","magnesium"]], y_train)
predictions = cls.predict(test[["refractive_index", "aluminum","magnesium"]])
print confusion_matrix(predictions,y_test)

cls.fit(train[["aluminum","magnesium"]], y_train)
predictions = cls.predict(test[["aluminum","magnesium"]])
print confusion_matrix(predictions,y_test)
#tested with some other options, for the flat vs container option, confusion matrix appears to be the same

#accuracy

test['pred_class'] = glass.aluminum.predict(test[['aluminum']])
accuracy = sum(test.pred_class == test.default) / float(len(test.default))
#I'm doing something wrong

#auc score
probs = cls.predict_proba(test[["aluminum","magnesium"]])[:, 1]
print metrics.roc_auc_score(y_test, probs)



'''
Part 4
'''

lin = LinearRegression()
scores = cross_val_score(lin, X, y, cv=10, scoring='mean_squared_error')
face = np.mean(np.sqrt(-scores))

probs = lin.predict_proba(test)[:, 1]
print metrics.roc_auc_score(y_test, face)
#something wrong 

#etc

#etc






