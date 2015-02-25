# -*- coding: utf-8 -*-
"""
Created on Mon Feb 02 19:15:27 2015

@author: abrown1
"""

import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt

DF = pd.read_csv('c:\class\dat4\dat4\data\ZYX_prices.csv')

# create two new metrics: percent change of the stock / minute, and tweet sentiment per tweet
X = pd.DataFrame(columns=['TS1','TS5','TS10','TS20','TS30','TS60','P1','P5','P10','P20','P30','P60'])
X['TS1'] = DF['ZYX1MinSentiment']/(DF['ZYX1MinTweets']+1e-10)
X['TS5'] = DF['ZYX5minSentiment']/(DF['ZYX5minTweets']+1e-10)
X['TS10'] = DF['ZYX10minSentiment']/(DF['ZYX10minTweets']+1e-10)
X['TS20'] = DF['ZYX20minSentiment']/(DF['ZYX20minTweets']+1e-10)
X['TS30'] = DF['ZYX30minSentiment']/(DF['ZYX30minTweets']+1e-10)
X['TS60'] = DF['ZYX60minSentiment']/(DF['ZYX60minTweets']+1e-10)
X['P1'] = DF['ZYX1minPriceChange']
X['P5'] = DF['ZYX5minPriceChange']
X['P10'] = DF['ZYX10minPriceChange']
X['P20'] = DF['ZYX20minPriceChange']
X['P30'] = DF['ZYX30minPriceChange']
X['P60'] = DF['ZYX60minPriceChange']

# create a results matrix
y = DF[DF.columns[-5:]]



#create models
LinReg = LinearRegression()

# explore results data
y.hist(bins = 40)
plt.xlim(-0.01,0.01)
plt.xlabel('percent change')
plt.ylabel('frequency')

yLin = y['60fret']
#create train test split for linear regression
X_train, X_test, y_train, y_test = train_test_split(X, yLin, random_state=1000)
LinReg.fit(X_train,y_train)
LinReg.score(X_test,y_test)

# LOGISTIC REGRESSION
binUp = np.where(y > 0.005, 1, 0)
binDown = np.where(y < -0.005, 1, 0)
binUp60 = np.where(y['60fret'] > 0.005, 1, 0)
binDown60 = np.where(y['60fret'] < -0.005, 1, 0)

LogReg = LogisticRegression()
#create train test split for logistic regression
X_train, X_test, binUp60_train, binUp60_test = train_test_split(X, binUp60, random_state=1000)
X_train, X_test, binDown60_train, binDown60_test = train_test_split(X, binDown60, random_state=1000)

LogReg.fit(X_train, binUp60_train)
LogReg.score(X_test, binUp60_test)
B1Up = LogReg.coef_
B2Up = LogReg.intercept_
predsUp = LogReg.predict(X_test)
print metrics.accuracy_score(binUp60_test, predsUp)
print metrics.confusion_matrix(binUp60_test, predsUp)
probs_up = LogReg.predict_proba(X_test)[:,1]
predict_up = np.where(probs_up > 0.055, 1, 0)
print metrics.accuracy_score(binUp60_test, predict_up)
print metrics.confusion_matrix(binUp60_test, predict_up)
print metrics.roc_auc_score(binUp60_test, probs_up)


LogReg.fit(X_train, binDown60_train)
LogReg.score(X_test, binDown60_test)
predsDown = LogReg.predict(X_test)