# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 21:56:20 2015

@author: deronhogans
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# can read a file directly from a URL
users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT4/master/data/u.user',\
sep='|', header=None, names=['user_id', 'age', 'gender', 'occupation', 'zip_code'],\
index_col='user_id')

print users
# read 'u.user' into 'users'


# examine the users data
users                   # print the first 30 and last 30 rows
type(users)             # DataFrame
users.head(3)            # print the first 5 rows
users.tail(3)            # print the last 5 rows
users.describe()        # summarize all numeric columns
users.index             # "the index" (aka "the labels")
users.columns           # column names (which is "an index")
users.dtypes            # data types of each column
users.shape             # number of rows and columns
users.values            # underlying numpy array
users.info()            # concise summary (includes memory usage as of pandas 0.15.0)

# select a column
users['gender']         # select one column
type(users['gender'])   # Series
users.gender            # select one column using the DataFrame attribute
users.zip_code
# summarize a single column
users.gender.describe()         # describe the gender Series (non-numeric)
users.gender.value_counts()     # for each gender, count number of occurrences

# summarize all columns (new in pandas 0.15.0)
users.describe(include='all')       # describe all Series
users.describe(include=['object'])  # limit to one (or more) types

# select multiple columns
users[['age', 'gender']]        # select two columns
my_cols = ['age', 'gender']     # or, create a list...
users[my_cols]                  # ...and use that list to select columns
type(users[my_cols])            # DataFrame

# simple logical filtering
users[users.age < 20]               # only show users with age < 20
young_bool = users.age < 20         # or, create a Series of booleans...
users[young_bool]                   # ...and use that Series to filter rows
users[users.age < 20].occupation    # select one column from the filtered results

# advanced logical filtering
users[users.age < 20][['age', 'occupation']]        # select multiple columns
users[(users.age < 20) & (users.gender=='M')]       # use multiple conditions
users[users.occupation.isin(['doctor', 'lawyer'])]  # filter specific values

# sorting
users.age.order()                           # only works for a Series
users.sort_index()                          # sort rows by label
users.sort_index(by='age')                  # sort rows by a specific column
users.sort_index(by='age', ascending=False) # use descending order instead
users.sort_index(by=['occupation', 'age'])  # sort by multiple columns

# detecting duplicate rows
users.duplicated()          # Series of booleans (True if a row is identical to a previous row)
users.duplicated().sum()    # count of duplicates
users[users.duplicated()]   # only show duplicates
users.drop_duplicates()     # drop duplicate rows
users.age.duplicated()      # check a single column for duplicates
users.duplicated(['age', 'gender', 'zip_code']).sum()   # specify columns for finding duplicates

users.groupby('occupation').mean().plot(kind='bar') # On average, Users above the age of 45 are Retired

m_cols = ['movie_id', 'title']
movies = pd.read_table('http://files.grouplens.org/datasets/movielens/ml-100k/u.item', header=None, names=m_cols, sep='|', usecols=[0, 1])
movies.head()
movies.shape

# read 'u.data' into 'ratings'
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_table('http://files.grouplens.org/datasets/movielens/ml-100k/u.data', header=None, names=r_cols, sep='\t')
ratings.head()
ratings.shape

# merge 'movies' and 'ratings' (inner join on 'movie_id')
movie_ratings = pd.merge(movies, ratings)
movie_ratings.head()
movie_ratings.shape

movie_ratings.groupby('movie_id').rating.mean().plot(kind='area') # Can easily identify the areas in the data where the movies with the highest ratings are located