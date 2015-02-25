Homework Glass dataset (Class 10)

# import necessary modules
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split

# 1 - Read in glass dataset, explore a bit, add column column names
glass_cols = ['ID', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'g_type']
glassdata = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data',
    header=None, names=glass_cols)
    
# Breifly explore the data
glassdata.dtypes
glassdata.info
glassdata.shape
glassdata.head()
glassdata.describe()
glassdata.g_type.value_counts()

# Create new feature called "binary' which creates two classes of glass
glassdata['binary'] = np.where(glassdata.g_type < 5, 0, 1)
glassdata.binary.count

# 2 Create 'X' using all features, and 'y' using ' binary' as explanatory variable
y = glassdata.binary
X = glassdata[['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']]

# Split into train and test, make X & y are correct
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)
X_train.shape
y_train.shape
X_test.shape
y_test.shape

# Convert back into dataframes
train = pd.DataFrame(data=X_train, columns=['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe'])
train['g_type'] = y_train
train = pd.DataFrame(data=X_test, columns=['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe'])
train['g_type'] = y_test
#Examine variables in training set
train.hist()

# Creaate scatterplots of each independent variable vs. dependent variable
train.plot(x='RI', y='g_type', kind='scatter')
#nope, doesn'make sense

# try comparing indeps to each other, then replicating what we did with Credit Data

train.plot(x='RI', y='Na', kind='scatter')
#'wg = 'window glass'; og = 'other glass'
train.wg = glassdata[glassdata.binary == 0]
train.og = glassdata[glassdata.binary == 1]

# explore the data a bit
plt.figure()
plt.scatter(train.wg.RI, train.wg.Na, alpha = .5, marker = '+', c= 'b')
plt.scatter(train.wg.RI, train.wg.Na, marker = 'w', edgecolors = 'r', facecolors = 'none')

#3 Fit a logistic regression model and make predictions 
model = LogisticRegression()
model.fit(X_train, y_train)
preds = model.predict(X_test)

probs = model.predict_proba(X_test)[:,1]

# Calculate accuracy
from sklearn import metrics
print metrics.accuracy_score(y_test, preds)

# print confusion matrix
print metrics.confusion_matrix(y_test, preds)

# nicer confusion matrix
from nltk import ConfusionMatrix
print ConfusionMatrix(list(y_test), list(preds))

#calculate acuracy 
from sklearn import metrics
print metrics.confusion_matrix(y_test, preds)
print metrics.accuracy_score(y_test,preds)

# Compare to null accuracy rate
print y_test
1-y_test.mean()

# calculate AUC
print metrics.roc_auc_score(y_test, probs)

# #4 Use cross validation (with AUC as scoring metric) to compare three models:
# logistic regression, KNN (K=1), KNN (K=3)

from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X,y)
knn.score(X,y)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X,y)
knn.score(X,y)

#calculate AUC
print metrics.roc_auc_score(y_test, probs)

logreg = LogisticRegression()
cross_val_score(logreg, X, y, cv=4, scoring='roc_auc').mean()

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X,y)
cross_val_score(knn, X, y, cv=4, scoring='roc_auc').mean()

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X,y)
cross_val_score(knn, X, y, cv=4, scoring='roc_auc').mean()

# And the winner is logistic regression, w auc=.946
# KNN with K = 3 is next with auc = .887 was 2nd, with KNN K = 1 last at .818

#5 Explore data to see if any features look like good predictors
# Also see if features that are helping with prediction can be eliminated
glassdata.groupby('binary').mean()
# features that look to be the most differentiaging are Na, Mg, Al, Ba.
# Re-run to see if using only these features increases accuracy

y = glassdata.binary
X = glassdata[['Na', 'Mg', 'Al', 'Ba']]
logreg = LogisticRegression()
cross_val_score(logreg, X, y, cv=4, scoring='roc_auc').mean()

# new auc is .987, which is better
# net, model can be improved by using only these 4 features to predict glass type