# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 19:26:02 2015

@author: deronhogans
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from nltk import ConfusionMatrix
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split, cross_val_score

oscorp_url = 'https://raw.githubusercontent.com/justmarkham/DAT4/master/data/ZYX_prices.csv'
oscorp_data = pd.read_table(oscorp_url, sep=',',index_col=None)

oscorp_data['Avg_60_Sent'] = oscorp_data.ZYX60minSentiment/oscorp_data.ZYX60minTweets

X = oscorp_data[['Avg_60_Sent', 'ZYX60minTweets','ZYX60minPriceChange']]
y = oscorp_data['60fret']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=3)


logreg = LogisticRegression() 
logreg.fit(X_train, y_train) 
preds = logreg.predict(X_test) 

print(ConfusionMatrix(list(y_test), list(preds)))