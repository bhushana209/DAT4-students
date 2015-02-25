# -*- coding: utf-8 -*-
"""
Created on Mon Feb 02 17:37:42 2015

@author: abrown1

Part 1:
Read the data into a DataFrame.
Briefly explore the data to make sure the DataFrame matches your expectations.
Create a new column called 'binary' that maps the glass type from 7 classes to 2 classes:
If type of glass = 1/2/3/4, binary = 0.
If type of glass = 5/6/7, binary = 1.
Part 2:
Create 'X' using all features, and create 'y' using the binary column.
Don't use the ID number or the glass type as features!
Split X and y into training and test sets.
Part 3:
Fit a logistic regression model on your training set, and make predictions on your test set.
Print the confusion matrix.
Calculate the accuracy and compare it to the null accuracy rate.
Calculate the AUC.
Part 4:
Use cross-validation (with AUC as the scoring metric) to compare these three models:
logistic regression
KNN (K = 1)
KNN (K = 3)
Part 5 (Optional):
Explore the data to see if any features look like good predictors.
Use cross-validation to compare a model with a smaller set of features with your best model from Part 4.

"""
# part 1
import numpy as np
import pandas as pd

glassN = pd.read_table('c:\class\dat4\glass.names')

glassDF = pd.read_table('c:\class\dat4\glass.data', header = None, sep=',', names=['id','ri','na','mg','al','si','k','ca','ba','fe','glass_type'], index_col='id')
#use the where function to create a new list for binary and add it to the dataframe
glassDF['binary'] = np.where(glassDF['glass_type'] > 5, 1, 0)

#part 2
from sklearn.cross_validation import train_test_split
features = glassDF.columns[:-2]
X = glassDF[features]
y = glassDF['binary']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1000)

# part 3
from sklearn.linear_model import LogisticRegression
glassType = LogisticRegression()
glassType.fit(X_train, y_train)
B1 = glassType.coef_[0]
B0 = glassType.intercept_[0]
glassType.score(X_test,y_test)

preds = glassType.predict(X_test)
from sklearn import metrics
print metrics.accuracy_score(y_test, preds)
print metrics.confusion_matrix(y_test, preds)
from nltk import ConfusionMatrix
print ConfusionMatrix(list(y_test), list(preds))

probs = glassType.predict_proba(X_test)[:, 1]
print metrics.roc_auc_score(y_test, probs)

#part 4
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score
LogReg = LogisticRegression()
KNN1 = KNeighborsClassifier(n_neighbors=1)
KNN3 = KNeighborsClassifier(n_neighbors=3)
CVscoreLogReg = cross_val_score(LogReg, X, y, cv=10, scoring = 'roc_auc').mean()
CVscoreKNN1 = cross_val_score(KNN1, X, y, cv=10, scoring = 'roc_auc').mean()
CVscoreKNN3 = cross_val_score(KNN3, X, y, cv=10, scoring = 'roc_auc').mean()

"""

1. Title: Glass Identification Database

2. Sources:
    (a) Creator: B. German
        -- Central Research Establishment
           Home Office Forensic Science Service
           Aldermaston, Reading, Berkshire RG7 4PN
    (b) Donor: Vina Spiehler, Ph.D., DABFT
               Diagnostic Products Corporation
               (213) 776-0180 (ext 3014)
    (c) Date: September, 1987

3. Past Usage:
    -- Rule Induction in Forensic Science
       -- Ian W. Evett and Ernest J. Spiehler
       -- Central Research Establishment
          Home Office Forensic Science Service
          Aldermaston, Reading, Berkshire RG7 4PN
       -- Unknown technical note number (sorry, not listed here)
       -- General Results: nearest neighbor held its own with respect to the
             rule-based system

4. Relevant Information:n
      Vina conducted a comparison test of her rule-based system, BEAGLE, the
      nearest-neighbor algorithm, and discriminant analysis.  BEAGLE is 
      a product available through VRS Consulting, Inc.; 4676 Admiralty Way,
      Suite 206; Marina Del Ray, CA 90292 (213) 827-7890 and FAX: -3189.
      In determining whether the glass was a type of "float" glass or not,
      the following results were obtained (# incorrect answers):

             Type of Sample                            Beagle   NN    DA
             Windows that were float processed (87)     10      12    21
             Windows that were not:            (76)     19      16    22

      The study of classification of types of glass was motivated by 
      criminological investigation.  At the scene of the crime, the glass left
      can be used as evidence...if it is correctly identified!

5. Number of Instances: 214

6. Number of Attributes: 10 (including an Id#) plus the class attribute
   -- all attributes are continuously valued

7. Attribute Information:
   1. Id number: 1 to 214
   2. RI: refractive index
   3. Na: Sodium (unit measurement: weight percent in corresponding oxide, as 
                  are attributes 4-10)
   4. Mg: Magnesium
   5. Al: Aluminum
   6. Si: Silicon
   7. K: Potassium
   8. Ca: Calcium
   9. Ba: Barium
  10. Fe: Iron
  11. Type of glass: (class attribute)
      -- 1 building_windows_float_processed
      -- 2 building_windows_non_float_processed
      -- 3 vehicle_windows_float_processed
      -- 4 vehicle_windows_non_float_processed (none in this database)
      -- 5 containers
      -- 6 tableware
      -- 7 headlamps

8. Missing Attribute Values: None

Summary Statistics:
Attribute:   Min     Max      Mean     SD      Correlation with class
 2. RI:       1.5112  1.5339   1.5184  0.0030  -0.1642
 3. Na:      10.73   17.38    13.4079  0.8166   0.5030
 4. Mg:       0       4.49     2.6845  1.4424  -0.7447
 5. Al:       0.29    3.5      1.4449  0.4993   0.5988
 6. Si:      69.81   75.41    72.6509  0.7745   0.1515
 7. K:        0       6.21     0.4971  0.6522  -0.0100
 8. Ca:       5.43   16.19     8.9570  1.4232   0.0007
 9. Ba:       0       3.15     0.1750  0.4972   0.5751
10. Fe:       0       0.51     0.0570  0.0974  -0.1879

9. Class Distribution: (out of 214 total instances)
    -- 163 Window glass (building windows and vehicle windows)
       -- 87 float processed  
          -- 70 building windows
          -- 17 vehicle windows
       -- 76 non-float processed
          -- 76 building windows
          -- 0 vehicle windows
    -- 51 Non-window glass
       -- 13 containers
       -- 9 tableware
       -- 29 headlamps



"""