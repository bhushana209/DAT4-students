# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 19:04:47 2015

@author: ganeshacharya
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

users = pd.read_table('../data/u.user', sep='|', header=None, names=['user_id', 'age', 'gender', 'occupation', 'zip_code'], index_col='user_id')
users
type(users)
users.head()
users.tail()
users.describe()
users.index
users.gender
help(users.sort_index)
drinks=pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT4/master/data/drinks.csv',sep=',')
drinks=pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT4/master/data/drinks.csv')
drinks
drinks.head(10)
drinks.dtypes
drinks['beer_servings']
drinks.beer_servings
drinks.info()
drinks.beer_servings.describe()
drinks.beer_servings.mean()
drinks[drinks.continent=='EU']
drinks[drinks.continent=='EU'].beer_servings.mean()
drinks[(drinks.continent=='EU' &.wine_servings
counts=pd.Series(234,456)