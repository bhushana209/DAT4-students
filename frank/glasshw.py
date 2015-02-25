import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

# creating column headers
cols =['id', 'refract_index', 'Sodium','Magnesium', 'aluminum', 'silicon', 'potassium', 'calcium', 'barium', 'iron', 'glass_type']

# read csv into a list of lists
data = pd.read_table('glassdata.csv', header=None, sep=',', names=cols, index_col='id')
# create column headers

# converting to a pandas dataframe
glass = pd.DataFrame(data)

# creating new binary column
glass['binary'] = glass.glass_type.map({1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:1})

# creating X and y columns
X = glass[['refract_index', 'Sodium','Magnesium', 'aluminum', 'silicon', 'potassium', 'calcium', 'barium', 'iron']]
y = glass['binary']

# creating test split
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# running logistic regression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
preds = logreg.predict(X_test)

# creating confusion matrix
from nltk import ConfusionMatrix
print ConfusionMatrix(list(y_test), list(preds))

accuracy = logreg.score(X_test, y_test)
y_test.mean()
1 - y_test.mean()

# calculate AUC
from sklearn import metrics
probs = logreg.predict_proba(X_test)[:, 1]
print metrics.roc_auc_score(y_test, probs)

# use AUC as evaluation metric for cross-validation
from sklearn.cross_validation import cross_val_score
cross_val_score(logreg, X, y, cv=10, scoring='roc_auc').mean()

# knn
from sklearn.neighbors import KNeighborsClassifier
knn1 = KNeighborsClassifier(n_neighbors=1)
knn1.fit(X, y)
cross_val_score(knn1, X, y, cv=10, scoring='roc_auc').mean()

knn3 = KNeighborsClassifier(n_neighbors=3)
knn3results = knn3.fit(X, y)
cross_val_score(knn3, X, y, cv=10, scoring='roc_auc').mean()


