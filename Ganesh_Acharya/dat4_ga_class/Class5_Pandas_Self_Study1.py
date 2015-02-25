# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 15:48:47 2015

@author: ganeshacharya
"""

import pandas as pd
import numpy as np
help(pd.set_option)
counts=pd.Series([632, 1638, 569, 115]) #eries is a single vector of data
counts # a Numpy array comprises the value of the series
counts=pd.Series([5,6,7],[2,3,4]) # Index is a pandas Object
counts #The array that follows the values array is assigned as an index
counts.values
counts.index
counts=pd.Series([2,3,4])
counts
counts.values
counts=pd.Series([2,3,4],[5,6,7],[8,9,10])
counts
bacteria = pd.Series([632, 1638, 569, 115], 
    index=['Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes'])
bacteria
bacteria['Actinobacteria']
bacteria[[name.endswith('bacteria') for name in bacteria.index]]# endswith is one of the string methods
[name.endswith('bacteria') for name in bacteria.index]
bacteria[0]
bacteria.name='counts'
bacteria.index.name='phylus'
bacteria
bacteria[bacteria>500]
bacteria_dict = {'Firmicutes': 632, 'Proteobacteria': 1638, 'Actinobacteria': 569, 'Bacteroidetes': 115}
pd.Series(bacteria_dict)
bacteria2 = pd.Series(bacteria_dict, index=['Cyanobacteria','Firmicutes','Proteobacteria','Actinobacteria'])
bacteria2 # Pandas use the Not a number type for missing values
bacteria2.isnull()
bacteria
bacteria2
bacteria+bacteria2 # the missing values are propogated by addition
data=pd.DataFrame({'value':[632, 1638, 569, 115, 433, 1130, 754, 555],
                     'patient':[1, 1, 1, 1, 2, 2, 2, 2],
                     'phylum':['Firmicutes', 'Proteobacteria', 'Actinobacteria', 
    'Bacteroidetes', 'Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes']}) # the dataframe is sorted by the column name
    
data
data[['value','patient','phylum']] 
data.columns # a dataframe has a second index for columns
data['value']
data.value
type(data['value'])
data.ix[3]# to extract a row using an index in a data frame
data = pd.DataFrame({0: {'patient': 1, 'phylum': 'Firmicutes', 'value': 632},
                    1: {'patient': 1, 'phylum': 'Proteobacteria', 'value': 1638},
                    2: {'patient': 1, 'phylum': 'Actinobacteria', 'value': 569},
                    3: {'patient': 1, 'phylum': 'Bacteroidetes', 'value': 115},
                    4: {'patient': 2, 'phylum': 'Firmicutes', 'value': 433},
                    5: {'patient': 2, 'phylum': 'Proteobacteria', 'value': 1130},
                    6: {'patient': 2, 'phylum': 'Actinobacteria', 'value': 754},
                    7: {'patient': 2, 'phylum': 'Bacteroidetes', 'value': 555}})#an alternative way of initializing dataframe
data
data = data.T
data
vals = data.value
vals
vals[5]=0
vals
vals=data.value.copy()
vals[5]=1000
data
data['year']=2013
data
treatment=pd.Series([0]*4+[1]*2)
treatment
data['treatment']=treatment
data
data['month']=['Jan']*len(data)
data
del data['month']
data
data.values
df = pd.DataFrame({'foo': [1,2,3], 'bar':[0.4, -1.0, 4.5]})
df.values
df = pd.DataFrame({'foo': [1,2,3], 'bar':[0.4, -1.0, 4.5]})
bacteria2.index = bacteria.index
bacteria2