'''
HOMEWORK: Model Evaluation
@author: laura egerdal
Created on Sat Jan 31 2015
'''

#    T H E   G L A S S I F I E R !  (aka glass classifier)

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from nltk import ConfusionMatrix

# Read the data into a DataFrame.
# source: http://archive.ics.uci.edu/ml/datasets/Glass+Identification
column_names = ['Id', 'RI', 'Na', 'Mg', 'AL', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'type']
data = pd.read_csv('data/glass.txt', names=column_names, index_col=0)

# Briefly explore the data to make sure the DataFrame matches your expectations.
# 214 rows, 10 columns
data.describe  
data.head()
data.tail()
data.shape

# Create a new column called 'binary' that maps the glass type from 7 classes to 2 classes:
# If type of glass = 1/2/3/4, binary = 0.
# If type of glass = 5/6/7, binary = 1.
data['binary'] = [ 0 if row <= 4 else 1 for row in data.type]

# Create 'X' using all features, and create 'y' using the binary column.
# Don't use the ID number or the glass type as features!
X = data[['RI', 'Na', 'Mg', 'AL', 'Si', 'K', 'Ca', 'Ba', 'Fe']]
y = data.binary

# Make sure shapes are correct
X.shape #(214,9)
y.shape #(214,)

# Split X and y into training and test sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
X_train.shape  #(160, 9)
X_test.shape   #(54, 9)
y_train.shape  #(160,)
y_test.shape   #(54,)

# Fit a logistic regression model on your training set, and make predictions on your test set.
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
preds = logreg.predict(X_test)

# Print the confusion matrix.
print ConfusionMatrix(list(y_test), list(preds))

# Calculate the accuracy and compare it to the null accuracy rate.
logreg.score(X_test, y_test)   
''' Accuracy: 94.44 '''

1 - y_test.mean()


# Calculate the AUC.

probs = logreg.predict_proba(X_test)[:, 1]
preds = np.where(probs > 0.5, 1, 0)  #defaults to 0.5

print ConfusionMatrix(list(y_test), list(preds))

# calculate the AUC  99.45
print metrics.roc_auc_score(y_test, probs)
''' AUC score: 99.45 '''

# Use cross-validation (with AUC as the scoring metric) to compare these three models:

# AUC score for logistic regression: 
cross_val_score(logreg, X, y, cv=10, scoring='roc_auc').mean()
''' AUC score: 95.75 '''

# AUC score for KNN (K = 1): 
knn = KNeighborsClassifier(n_neighbors=1)
cross_val_score(knn, X, y, cv=10, scoring='roc_auc').mean()
''' AUC score: 90.19 '''

# AUC score for KNN (K = 3): 
knn = KNeighborsClassifier(n_neighbors=3)
cross_val_score(knn, X, y, cv=10, scoring='roc_auc').mean()
''' AUC score:  93.14 '''


''' 

Part 5 (Optional):
Explore the data to see if any features look like good predictors.
Use cross-validation to compare a model with a smaller set of features with your best model from Part 4.
'''
# scatterplot matrix of all numerical columns
plt.clf
pd.scatter_matrix(data)

plt.clf
data.corr()



# histograms for each feature for the 2 different responses
plt.clf
data.RI.hist(by=data.binary, sharex=True)
data.Na.hist(by=data.binary, sharex=True)
data.Mg.hist(by=data.binary, sharex=True)
data.AL.hist(by=data.binary, sharex=True)
data.Si.hist(by=data.binary, sharex=True)
data.K.hist(by=data.binary, sharex=True)
data.Ca.hist(by=data.binary, sharex=True)
data.Ba.hist(by=data.binary, sharex=True)
data.Fe.hist(by=data.binary, sharex=True)

# comparing the range, mean and median of each feature, grouped by the 2 different responses
feature_names = ['RI', 'Na', 'Mg', 'AL', 'Si', 'K', 'Ca', 'Ba', 'Fe']
for item in feature_names:
    min_val_0 = data[data.binary == 0][item].min()
    min_val_1 = data[data.binary == 1][item].min()
    max_val_0 = data[data.binary == 0][item].max()
    max_val_1 = data[data.binary == 1][item].max()
    mean_val_0 = data[data.binary == 0][item].mean()
    mean_val_1 = data[data.binary == 1][item].mean()
    median_val_0 = data[data.binary == 0][item].median()
    median_val_1 = data[data.binary == 1][item].median()
    mean_dif = (data[data.binary == 0][item].mean() - data[data.binary == 1][item].mean()) / (data[item].max() - data[item].min())*100
    median_dif = (data[data.binary == 0][item].median() - data[data.binary == 1][item].median()) / (data[item].max() - data[item].min())*100

    print 'When binary is 0,', item, 'ranges from' , min_val_0, 'to', max_val_0
    print 'When binary is 1,', item, 'ranges from' , min_val_1, 'to', max_val_1
    print 'When binary is 0,', item, 'mean is ' , mean_val_0
    print 'When binary is 1,', item, 'mean is' , mean_val_1
    print 'When binary is 0,', item, 'median is ' , median_val_0
    print 'When binary is 1,', item, 'median is' , median_val_1
    print 'The change in mean is ', mean_dif, 'percent of the total value range.'
    print 'The change in median is ', median_dif, 'percent of the total value range.'
    print ' '
    print ' '


# I think the features with the strongest relationship are possibily:
# Mg, AL

# assign these two features to X
X = data[['Mg', 'AL']]

# Split X and y into training and test sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# Fit a logistic regression model; make predictions
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
preds = logreg.predict(X_test)

# Calculate the accuracy
logreg.score(X_test, y_test)
''' Accuracy: 90.74 (decreased from 94.44) '''

# Calculate the AUC.
probs = logreg.predict_proba(X_test)[:, 1]
print metrics.roc_auc_score(y_test, probs)
''' AUC score: 97.55 (decreased from 99.45) '''


# Use cross-validation (with AUC as the scoring metric) to compare these three models:

# AUC score for logistic regression: 
cross_val_score(logreg, X, y, cv=10, scoring='roc_auc').mean() 
''' AUC score: 98.50 (INCREASED from 95.75) '''

# AUC score for KNN (K = 1): 90.19
knn = KNeighborsClassifier(n_neighbors=1)
cross_val_score(knn, X, y, cv=10, scoring='roc_auc').mean()
''' AUC score: 84.01 (decreased from 90.19) '''

# AUC score for KNN (K = 3): 93.14
knn = KNeighborsClassifier(n_neighbors=3)
cross_val_score(knn, X, y, cv=10, scoring='roc_auc').mean()
''' AUC score: 89.89 (decreased from 93.14) '''