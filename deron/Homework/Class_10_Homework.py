import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from nltk import ConfusionMatrix
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split, cross_val_score

# Read in Data
features = ['ID', 'RI', 'Sodium', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'type_of_glass']
glass_data_url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data'
glass_data = pd.read_table(glass_data_url, sep=',', names=features, index_col='ID')

# Add 'Binary' to data
glass_data['binary'] = glass_data.type_of_glass.map({1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:1})

# Set X, y
X = glass_data[features[1:-1]]
y = glass_data.binary

# Split train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=5)

# Build Logistic Regression model
logreg = LogisticRegression() 
logreg.fit(X_train, y_train) 
preds = logreg.predict(X_test) 

# Print Confusion Matrix
print(ConfusionMatrix(list(y_test), list(preds)))

# print Accuracy
print metrics.accuracy_score(y_test, preds)

# Compare Scores of logReg, KNN=1, and KNN=3
scores = cross_val_score(logreg, X, y, cv=10, scoring='mean_squared_error')
np.mean(np.sqrt(-scores))

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
scores_KNN_One = cross_val_score(knn, X, y, cv=10, scoring='mean_squared_error')
np.mean(np.sqrt(-scores_KNN_One))

from sklearn.neighbors import KNeighborsClassifier
knn2 = KNeighborsClassifier(n_neighbors=3)
scores_KNN_Two = cross_val_score(knn2, X, y, cv=10, scoring='mean_squared_error')
np.mean(np.sqrt(-scores_KNN_Two))
