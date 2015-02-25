# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 18:23:44 2015

@author: ganeshacharya
"""

import numpy as np
# read in the iris data
from sklearn.datasets import load_iris
iris=load_iris() #assign the data set to a variable
#note - X is in caps indicating it might have multiple features
iris
X,y=iris.data, iris.target # assign values to 2 variables
X.shape
y.shape
iris.feature_names
iris.target
iris.target_names
from sklearn.neighbors import KNeighborsClassifier # import class
knn = KNeighborsClassifier(n_neighbors=1) # instantiate the estimator
knn.fit(X,y) # fit with data
knn.predict([3,5,4,2])
iris.target_names[knn.predict([3,5,4,2])]
knn.predict([3,5,2,2])
X_new=[[3,5,4,2],[3,5,2,2]]
knn.predict(X_new)
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X,y)
knn.predict(X_new)
knn.predict_proba(X_new) # predicted probability of class membership. probabilities by 3 classes
knn.kneighbors([3,5,4,2]) # distance to nearest neighbors and identities
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X,y)
knn.score(X,y) #tell me how close your predicted values are to actual values
knn=KNeighborsClassifier(n_neighbors=1) # it is not a useful thing. Remove it
knn.fit(X,y) # its a 100% becos it is looking at distance to itself
knn.score(X,y) 
