
## Class 10 Homework: Model Evaluation




import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from nltk import ConfusionMatrix

#set headers for the dataframe
headers = ['ID num', 'Ref Index', 'Sodium', 'Mag', 'Alum', 'Silicon', 'Potassium', 'Calcium', 'Barium', 'Iron', 'Type']
#read data from CSV into the dataframe
glass_data = pd.read_csv('/Users/roellk/Desktop/Python/DAT4-students/david/glass.data', header=None, names=headers)
glass_data.columns = headers

#basic data exploration
print 'type\n', "*"*10
print type(glass_data)
print 'head\n', "*"*10
print glass_data.head()
print 'shape\n', "*"*10
print glass_data.shape
print 'describe\n', "*"*10
print glass_data.describe
print 'dtypes\n', "*"*10
print glass_data.dtypes
print 'values\n', "*"*10
print glass_data.values

#add a binary column to the dataframe for holding glass types 1-4 and 5-7
glass_data['binary'] = 1
glass_data.loc[glass_data.Type.between(1, 4), 'binary'] = 0
glass_data.loc[glass_data.Type.between(5, 7), 'binary'] = 1
print glass_data.head()
print glass_data.tail()
#print glass_data[(glass_data.Type > 2) & (glass_data.Type < 7)]


#part 2
X = glass_data[['Ref Index', 'Sodium', 'Mag', 'Alum', 'Silicon', 'Potassium', 'Calcium', 'Barium', 'Iron']]
y = glass_data.binary

#print X.shape
#print y.shape
#set up train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


#part 3
#fit the model
LR = LogisticRegression()
LR.fit(X_train, y_train)
score = LR.score(X_test, y_test)
print score, "model accuracy score" #score: 0.94444

#make predictions
preds = LR.predict(X_test)
print "Predictions for X_test\n", preds
print "Actual y_test\n", y_test
probs = LR.predict_proba(X_test)
#print "probabilities for LR test\n", probs

# predict in one step, calculate accuracy in a separate step
from sklearn import metrics
print "accuracy score\n", metrics.accuracy_score(y_test, preds)

#null accuracy rate
print "y_test mean\n", y_test.mean() #0.148148148148
print "1-y_test mean\n", 1-y_test.mean() #0.851851851852

print "ugly confusion matrix\n", metrics.confusion_matrix(y_test, preds)

print "pretty confusion matrix\n", ConfusionMatrix(list(y_test), list(preds))


# predict probabilities
probs = LR.predict_proba(X_test)[:, 1]
plt.hist(probs)
plt.show()

# plot ROC curve
fpr, tpr, thresholds = metrics.roc_curve(y_test, probs)
plt.plot(fpr, tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')
plt.show()

#calculate AUC
print "AUC: ", metrics.roc_auc_score(y_test, probs)

# part 4
#compare models LogReg, KNN-1, KNN-3
#Logistic Regression Model
LR = LogisticRegression()
print cross_val_score(LR, X, y, cv=3, scoring='roc_auc').mean() # AUC 0.939354

#KNN - 1
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
print cross_val_score(knn, X, y, cv=3, scoring='roc_auc').mean() # AUC 0.821532

#KNN - 3
knn = KNeighborsClassifier(n_neighbors=3)
print cross_val_score(knn, X, y, cv=3, scoring='roc_auc').mean() # AUC 0.879533



'''* Part 5 (Optional):
    * Explore the data to see if any features look like good predictors.
    * Use cross-validation to compare a model with a smaller set of features with your best model from Part 4.
'''