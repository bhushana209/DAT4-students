## Class 10 Homework: Model Evaluation
## Alex Lee
## 1/30/2015

## Imports and setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt  # for my system
from nltk import ConfusionMatrix
from sklearn import metrics
from sklearn.cross_validation import train_test_split, cross_val_score

## Part 1

# get column names from this site:
# http://archive.ics.uci.edu/ml/datasets/Glass+Identification
cols = ['ID', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']
data_url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data'
data = pd.read_table(data_url, sep=',', names=cols)

# create a new column, "binary", that maps the Type column into 2 bins:
data['binary'] = [0 if data['Type'][x] in {1, 2, 3, 4} else 1 for x in range(len(data))]

## Part 2

X = data[cols[1:-1]]
y = data.binary

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=123)

## Part 3

from sklearn.linear_model import LogisticRegression     # import the estimator we want
logreg = LogisticRegression()                           # instantiate estimator
logreg.fit(X_train, y_train)                            # fit with training data
preds = logreg.predict(X_test)                          # predict for test data
probs = logreg.predict_proba(X_test)                    # predict probabilities for AUC

print(ConfusionMatrix(list(y_test), list(preds)))       # see how we did

print(metrics.accuracy_score(y_test, preds))            # check accuracy (88.89%)

print(metrics.roc_auc_score(y_test, probs[:,1]))        # check AUC (93.98%)

## Part 4

# train first model (logistic regression):
mod1 = LogisticRegression()
scores1 = cross_val_score(mod1, X, y, cv=5, scoring='roc_auc')

# train second model (KNN, K=1):
from sklearn.neighbors import KNeighborsClassifier
mod2 = KNeighborsClassifier(n_neighbors=1)
scores2 = cross_val_score(mod2, X, y, cv=5, scoring='roc_auc')

# train third model (KNN, K=3):
mod3 = KNeighborsClassifier(n_neighbors=3)
scores3 = cross_val_score(mod3, X, y, cv=5, scoring='roc_auc')

# check the scores of the three models (average AUC over 5 folds of CV):
print "Logistic Regression:\t%.2f \nKNN, K=1:\t\t%.2f \nKNN, K=3:\t\t%.2f" % (np.mean(scores1), np.mean(scores2), np.mean(scores3))

# based on these scores, logistic regression is performing the best

## Part 5

# quick visual analysis:
pd.scatter_matrix(data)

# hand-picked features that look more correlated with binary:
sub_cols = ['RI', 'Mg', 'Al', 'Ca', 'Ba', 'Fe']

# test a new model on subset using logistic regression (best performer in part 4)
mod4 = LogisticRegression()
scores4 = cross_val_score(mod4, X[sub_cols], y, cv=5, scoring='roc_auc')

# check how we did vs. prior models:
print "Logistic Regression:\t%.2f \nKNN, K=1:\t\t%.2f \nKNN, K=3:\t\t%.2f \n\nMy model:\t\t%.2f" % (np.mean(scores1), np.mean(scores2), np.mean(scores3), np.mean(scores4))

# This does indeed show slight improvement in AUC (97% vs. 94% when including all columns)
