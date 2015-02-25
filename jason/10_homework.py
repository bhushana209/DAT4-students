# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 17:22:58 2015

@author: Jason
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# Step 1: Read in and explore data
data = '/Users/Jason/Documents/DataScience/DAT4-students/jason/data/glass.data'
headers = ['id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']

glass = pd.read_csv(data, header = None, names = headers, index_col = 'id')

glass.shape
glass.columns
glass.describe()
glass.duplicated()
glass.head()
glass.info()

# Create binary column
glass['binary'] = np.where(glass['Type'] < 5, 0, 1)
glass.binary.value_counts()
glass.binary.hist()

# Step 2: train_test_split
X = glass[['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']]
y = glass['binary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3,
                                                    random_state = 1)

# Step 3: Fit logistic regression and calculate accuracy
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
logreg.score(X_test, y_test) # Accuracy score = 0.9538461538461539
y_test.mean() # 0.18461538461538463
1 - y_test.mean() # 0.81538461538461537

preds = logreg.predict(X_test)
print metrics.confusion_matrix(y_test, preds)

probs = logreg.predict_proba(X_test)[:, 1]
plt.hist(probs)

preds = np.where(probs > 0.5, 1, 0)
print metrics.confusion_matrix(y_test, preds)   
                '''
                [[50  3]
                 [ 0 12]]
                '''

print metrics.accuracy_score(y_test, preds) # Accuracy score = 0.9538461538461539
print metrics.recall_score(y_test, preds) # Sensitivity = 0.916666666667
50 / float(50 + 3) # Specificity = 0.9433962264150944

fpr, tpr, thresholds = metrics.roc_curve(y_test, probs)
plt.plot(fpr, tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')

print metrics.roc_auc_score(y_test, probs) # AUC = 0.990566037736

# Step 4: Use cross-validation
X = glass[['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']]
y = glass['binary']
logreg = LogisticRegression()
cross_val_score(logreg, X, y, cv=10, scoring='roc_auc').mean() # 0.95754901960784322

knn1 = KNeighborsClassifier(n_neighbors = 1)
cross_val_score(knn1, X, y, cv=10, scoring='roc_auc').mean() # 0.90187500000000009

knn3 = KNeighborsClassifier(n_neighbors = 3)
cross_val_score(knn3, X, y, cv=10, scoring='roc_auc').mean() # 0.9313970588235293

# Step 5: Feature selection

glass.groupby('Type').RI.mean() # not distinctive
glass.groupby('Type').Na.mean() # maybe
glass.groupby('Type').Mg.mean() # distinctive
glass.groupby('Type').Al.mean() # distinctive
glass.groupby('Type').Si.mean() # not distinctive
glass.groupby('Type').K.mean() # distinctive
glass.groupby('Type').Ca.mean() # distinctive
glass.groupby('Type').Ba.mean() # distinctive
glass.groupby('Type').Fe.mean() # maybe

X = glass[['Na', 'Mg', 'Al', 'K', 'Ca', 'Ba', 'Fe']]
y = glass['binary']
logreg = LogisticRegression()
cross_val_score(logreg, X, y, cv=10, scoring='roc_auc').mean() # 0.95379901960784319

X = glass[['Mg', 'Al', 'K', 'Ca', 'Ba']]
y = glass['binary']
logreg = LogisticRegression()
cross_val_score(logreg, X, y, cv=10, scoring='roc_auc').mean() # 0.97750000000000004

