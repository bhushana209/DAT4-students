# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 16:38:01 2015

@author: deronhogans
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT4/master/data/drinks.csv') 
# Read in drinks.csv and set equal 
print drinks # Print users 

drinks                  # print the first 30 and last 30 rows
type(drinks)             # DataFrame
drinks.head()            # print the first 5 rows
drinks.tail()            # print the last 5 rows
drinks.describe()        # summarize all numeric columns
drinks.index             # "the index" (aka "the labels")
drinks.columns           # column names (which is "an index")
drinks.dtypes            # data types of each column
drinks.shape             # number of rows and columns
drinks.values            # underlying numpy array
drinks.info()            # concise summary (includes memory usage as of pandas 0.15.0)

# select a column
drinks['beer_servings']         # select one column
type(drinks['beer_servings'])   # Series
drinks.beer_servings            # select one column using the DataFrame attribute
drinks.wine_servings
# summarize a single column
drinks.continent.describe()         # describe the gender Series (non-numeric)
drinks.continent.value_counts()     # for each gender, count number of occurrences

# select multiple columns
drinks[['beer_servings', 'wine_servings']]        # select two columns
my_cols = ['beer_servings', 'wine_servings']     # or, create a list...
drinks[my_cols]                  # ...and use that list to select columns
type(drinks[my_cols])            # DataFrame

# simple logical filtering
drinks[drinks.beer_servings < 500]               # only show users with age < 20
young_bool = drinks.beer_servings < 500         # or, create a Series of booleans...
drinks[young_bool]                   # ...and use that Series to filter rows
drinks[drinks.beer_servings < 500].continent  # select one column from the filtered results

# advanced logical filtering
drinks[drinks.beer_servings < 500][['continent', 'total_litres_of_pure_alcohol']]        # select multiple columns
drinks[(drinks.beer_servings > 100) & (drinks.continent=='EU')]       # use multiple conditions
drinks[drinks.beer_servings.isin(['Iceland', 'Ireland'])]  # filter specific values

# sorting
drinks.wine_servings.order()                           # only works for a Series
drinks.sort_index()                          # sort rows by label
drinks.sort_index(by='beer_servings')                  # sort rows by a specific column
drinks.sort_index(by='beer_servings', ascending=False) # use descending order instead
drinks.sort_index(by=['continent', 'beer_servings'])  # sort by multiple columns

# find missing values in a Series
drinks.continent.isnull()           # True if NaN, False otherwise
drinks.continent.notnull()          # False if NaN, True otherwise
drinks[drinks.continent.notnull()]  # only show rows where continent is not NaN
drinks.continent.isnull().sum()     # count the missing values

# find missing values in a DataFrame
drinks.isnull()             # DataFrame of booleans
drinks.isnull().sum()    

# drop missing values
drinks.dropna()             # drop a row if ANY values are missing
drinks.dropna(how='all') 

# fill in missing values
drinks.continent.fillna(value='NA')                 # does not modify 'drinks'
drinks.continent.fillna(value='NA', inplace=True)   # modifies 'drinks' in-place
drinks.fillna(drinks.mean())                        # fill in missing values using mean


colors = np.where(drinks.continent=='NA', 'r', 'b')
drinks.plot(x='beer_servings', y='wine_servings', kind='scatter', c=colors)

drinks.beer_servings.hist(by=drinks.continent)

drinks.groupby('continent').wine_servings.mean().plot(kind='bar')
plt.ylabel('Average Number of Wine Servings Per Year') # Europeans consume a considerably hire amount of wine than all other continents

drinks.groupby('continent').total_litres_of_pure_alcohol.max().plot(kind='area')
plt.ylabel('Highest Total Litres of Pure Alcohol Consumed Per Year') # And Europeans seem to consume hte most alcohol pn average