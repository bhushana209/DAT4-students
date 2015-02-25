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