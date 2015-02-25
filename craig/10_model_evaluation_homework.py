# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 11:27:26 2015

@author: craig.m.lennon
"""


import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn import metrics
from nltk import ConfusionMatrix


col_names = ('id_number', 'index_of_refraction', 'na', 'mg', 'al', 'si', 'k', 'ca', 'ba', 'fe', 'glass_type')
glass = pd.read_table('C:\Users\Craig\Documents\Python_DS\GA_DS\DAT4-students\craig\glass.data', sep = ',', names = col_names)
glass_target_names = {1 : 'building_windows_float_processed', 2:'building_windows_non_float_processed',3 : 'vehicle_windows_float_processed', 4 : 'vehicle_windows_non_float_processed',5 : 'containers', 6:  'tableware',7: 'headlamps'}
glass['binary'] = np.where(glass.glass_type.isin([1,2,3,4]), 0, 1)

# define features and response. X and y respectively by convention.
X = glass[['index_of_refraction', 'na', 'mg', 'al', 'si', 'k', 'ca', 'ba', 'fe']]
#y = glass['glass_type']
y = glass['binary']


X.shape
y.shape

# Create the test and training sets using train test split
# set random_state to two for reproducibility

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 2)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# predict and caclculate accuracy
logreg.score(X_test, y_test) # compare the model predictions on the test data to real outcomes

# Save the predictions, needed for the confusion matrix

preds = logreg.predict(X_test) 

# print confusion matrix
#sklearn's confusion matrix
# print metrics.confusion_matrix(y_test, preds) 

# I agree with Kevin, the nltk ConfusionMatrix is more informative
print ConfusionMatrix(list(y_test), list(preds))

# Accuracy: Overall, how often is the model correct

accuracy = (39. + 9.) / (39. + 9 + 1 + 5) # Accuracy calculated manually from confusion matrix

print accuracy
print 1 - accuracy


print metrics.accuracy_score(y_test, preds) # Accuracy score from sklearn



# Sensitivity: when actual value is one, how often is the prediction correct?

print 9./(9. + 5. ) # calculated sentitivity manually using the confusion matrix values.
print metrics.recall_score(y_test, preds) # or...use sklearn's recall_score


# predict probabilities and calculate the AUC

probs = logreg.predict_proba(X_test)[:, 1]
print metrics.roc_auc_score(y_test, probs)


logreg = LogisticRegression()
scores_logreg = cross_val_score(logreg, X, y, cv = 5, scoring = 'roc_auc')
scores_logreg
print np.mean(scores_logreg)

knn = KNeighborsClassifier(n_neighbors = 1) # n = 5 by default
scores_knn_1 = cross_val_score(knn, X, y, cv = 5, scoring = 'roc_auc')
scores_knn_1
print np.mean(scores_knn_1)

knn = KNeighborsClassifier(n_neighbors = 3) 
scores_knn_3 = cross_val_score(knn, X, y, cv = 5, scoring = 'roc_auc')
scores_knn_3
print np.mean(scores_knn_3)

score_compare = {'Logistic Regression':np.mean(scores_logreg),'KNN, K =1':np.mean(scores_knn_1), 'KNN, K =3':np.mean(scores_knn_3)}


