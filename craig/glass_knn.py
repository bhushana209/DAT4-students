# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 16:06:02 2015

@author: craig.m.lennon
"""

import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.neighbors import KNeighborsClassifier #1. import class
from sklearn.cross_validation import train_test_split


col_names = ('id_number', 'index_of_refraction', 'na', 'mg', 'al', 'si', 'k', 'ca', 'ba', 'fe', 'glass_type')
glass = pd.read_table('C:\Users\Craig\Documents\Python_DS\GA_DS\DAT4-students\craig\glass.data', sep = ',', names = col_names)
glass_target_names = {1 : 'building_windows_float_processed', 2:'building_windows_non_float_processed',3 : 'vehicle_windows_float_processed', 4 : 'vehicle_windows_non_float_processed',5 : 'containers', 6:  'tableware',7: 'headlamps'}


# define features and response. X and y respectively by convention.
X = glass[['index_of_refraction', 'na', 'mg', 'al', 'si', 'k', 'ca', 'ba', 'fe']]
y = glass['glass_type']

X.shape
y.shape

# Create the test and training sets

X_train, X_test, y_train, y_test = train_test_split(X, y)



# 2. Instantiate the estimator

knn = KNeighborsClassifier() # n = 5 by default

# 3.  fit training data with n = 5
knn.fit(X_train, y_train)
knn.score(X_test, y_test)

# 4. refit with a different nearest neighbors value
knn = KNeighborsClassifier(n_neighbors = 3) # n = 5 by default

# fit training data with n = 3
knn.fit(X_train, y_train)
knn.score(X_test, y_test)

# n = 3 is the better model

# Train on all the data with best model

knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X, y)

# Make predictions on out of sample data

out_of_sample = [1.5234, 13.78, 4.89, 1.10, 72.45, 0.55, 8.75, 0, .3]
knn.predict(out_of_sample)
glass_target_names[knn.predict(out_of_sample)[0]]
knn.predict_proba(out_of_sample)