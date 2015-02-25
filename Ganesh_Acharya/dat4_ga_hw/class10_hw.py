# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 20:21:39 2015

@author: ganeshacharya
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
#Part 1 - Data exploration
pd.read_table('../data/glass_data.txt')
#assign column names
ga_col_names = ['id_number','Ri','Na', 'Mg','Al','Si', 'K', 'Ca','Ba','Fe','Type_glass']
#read glass_data in df
glassdata=pd.read_table('http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data',
                 header=None,names=ga_col_names,index_col='id_number',sep=',',na_values=['na','-',' '],
                dtype={'Type_glass':str})
glassdata
glassdata.head()    
glassdata.tail()
glassdata.describe()
glassdata.index
glassdata.columns
glassdata.dtypes
glassdata.shape
glassdata.values
glassdata.info
glassdata['Type_glass']
type(glassdata['Type_glass'])
glassdata.Type_glass
glassdata[['Ri','Na']]
glassdata[glassdata.Ri<1.5]
glassdata[glassdata.Ri<1.51834]
glassdata[glassdata.Ri<1.51834].Type_glass
glassdata[(glassdata.Type_glass=='7')&(glassdata.Ri>1.518)][['Ri','Type_glass']]
glassdata[glassdata.Type_glass.isin(['1','7'])]
glassdata.sort_index(inplace=True)
glassdata.sort_index()
glassdata.sort_index(axis=1)
glassdata.sort_index(by='Mg', ascending=False)
glassdata.duplicated()
glassdata.duplicated().sum() 
glassdata[glassdata.duplicated()]
glassdata.Al.duplicated().sum()
glassdata[glassdata.Al.duplicated()]
glassdata.sort_index(by='Si').tail(10)
glassdata.sort_index(by='Si', ascending=False).head(10)
glassdata[glassdata.Si==glassdata.Si.max()].Type_glass
glassdata.isnull()
glassdata.notnull()
num_col=glassdata.columns[1:5]
glassdata[num_col]=glassdata[num_col].astype('float')
glassdata.info()
bincheck='1' or '2' or '3' or '4'
glassdata['binary']=glassdata['Type_glass'].map(lambda x: 0 if x==bincheck else 1)
glassdata.binary
glassdata.loc[70:80]
glassdata.shape
# Part 2 - creating X and y
df = pd.DataFrame(glassdata, columns=ga_col_names)
X,y=glassdata[['Ri','Na', 'Mg','Al','Si', 'K', 'Ca','Ba','Fe']],glassdata['binary']
X.shape
y.shape
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
train = pd.DataFrame(data=X_train, columns=['Ri','Na', 'Mg','Al','Si', 'K', 'Ca','Ba','Fe'])
train['default'] = y_train
test = pd.DataFrame(data=X_test, columns=['Ri','Na', 'Mg','Al','Si', 'K', 'Ca','Ba','Fe'])
test['default'] = y_test
clf = LogisticRegression()
clf.fit(train[['Ri','Na', 'Mg','Al','Si', 'K', 'Ca','Ba','Fe']], y_train)
prob = clf.predict(pd.DataFrame(data=X_test))
prob
clf.score(X_test, y_test)
from nltk import ConfusionMatrix
print ConfusionMatrix(list(y_test), list(prob))
y_test.mean()
1 - y_test.mean()
fpr, tpr, thresholds = metrics.roc_curve(y_test, prob)
plt.plot(fpr, tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')
probs1=clf.predict_proba(X_test)[:,1]
# calculate AUC
print metrics.roc_auc_score(y_test, prob)
from sklearn.neighbors import KNeighborsClassifier  
knn_1 = KNeighborsClassifier(n_neighbors=1)           
knn_1.fit(X_train, y_train)                                       
knn_1.predict(X_test) 
knn_1.score(X_test,y_test)
knn_5 = KNeighborsClassifier(n_neighbors=5)           
knn_5.fit(X_train, y_train)                                       
knn_5.predict(X_test)      
knn_5.score(X_test,y_test)       
from sklearn.cross_validation import cross_val_score

cross_val_score(clf, X_test, y_test, cv=10, scoring='roc_auc').mean()    
cross_val_score(knn_1, X_test, y_test, cv=10, scoring='roc_auc').mean()     
cross_val_score(knn_5, X_test, y_test, cv=10, scoring='roc_auc').mean()        
