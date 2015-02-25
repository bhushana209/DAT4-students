# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 10:04:02 2015

@author: jen_lambert13
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)

names = ['imdbID', 'title', 'year', 'score', 'votes', 'runtime', 'genres']
data = pd.read_csv('https://raw.githubusercontent.com/cs109/content/master/imdb_top_10000.txt', delimiter='\t', names=names).dropna()
print "Number of rows: %i" % data.shape[0]
data.head()  # print the first 5 rows

dirty = '142 mins.'
number, text = dirty.split(' ')
clean = int(number)
print number

clean_runtime = [float(r.split(' ')[0]) for r in data.runtime]
data['runtime'] = clean_runtime
data.head()

#determine the unique genres
genres = set()
for m in data.genres:
    genres.update(g for g in m.split('|'))
genres = sorted(genres)

#make a column for each genre
for genre in genres:
    data[genre] = [genre in movie.split('|') for movie in data.genres]
         
data.head()

data['title'] = [t[0:-7] for t in data.title]
data.head()

data[['score', 'runtime', 'year', 'votes']].describe()

#hmmm, a runtime of 0 looks suspicious. How many movies have that?
print len(data[data.runtime == 0])

#probably best to flag those bad data as NAN
data.runtime[data.runtime==0] = np.nan

data.runtime.describe()

# more movies in recent years, but not *very* recent movies (they haven't had time to receive lots of votes yet?)
plt.hist(data.year, bins=np.arange(1950, 2013), color='#cccccc')
plt.xlabel("Release Year")
remove_border()

plt.hist(data.score, bins=20, color='#cccccc')
plt.xlabel("IMDB rating")

plt.hist(data.runtime.dropna(), bins=50, color='#cccccc')
plt.xlabel("Runtime distribution")

plt.scatter(data.year, data.score, lw=0, alpha=.08, color='k')
plt.xlabel("Year")
plt.ylabel("IMDB Rating")

plt.scatter(data.votes, data.score, lw=0, alpha=.2, color='k')
plt.xlabel("Number of Votes")
plt.ylabel("IMDB Rating")
plt.xscale('log')

# low-score movies with lots of votes
data[(data.votes > 9e4) & (data.score < 5)][['title', 'year', 'score', 'votes', 'genres']]

data[data.score == data.score.min()][['title', 'year', 'score', 'votes', 'genres']]

# The highest rated movies
data[data.score == data.score.max()][['title', 'year', 'score', 'votes', 'genres']]

#sum sums over rows by default
genre_count = np.sort(data[genres].sum())[::-1]
pd.DataFrame({'Genre Count': genre_count})

genre_count = data[genres].sum(axis=1) 
print "Average movie has %0.2f genres" % genre_count.mean()
genre_count.describe()

decade =  (data.year // 10) * 10

tyd = data[['title', 'year']]
tyd['decade'] = decade

tyd.head()


#mean score for all movies in each decade
decade_mean = data.groupby(decade).score.mean()
decade_mean.name = 'Decade Mean'
print decade_mean

plt.plot(decade_mean.index, decade_mean.values, 'o-',
        color='r', lw=3, label='Decade Average')
plt.scatter(data.year, data.score, alpha=.04, lw=0, color='k')
plt.xlabel("Year")
plt.ylabel("Score")
plt.legend(frameon=False)

grouped_scores = data.groupby(decade).score

mean = grouped_scores.mean()
std = grouped_scores.std()

plt.plot(decade_mean.index, decade_mean.values, 'o-',
        color='r', lw=3, label='Decade Average')
plt.fill_between(decade_mean.index, (decade_mean + std).values,
                 (decade_mean - std).values, color='r', alpha=.2)
plt.scatter(data.year, data.score, alpha=.04, lw=0, color='k')
plt.xlabel("Year")
plt.ylabel("Score")
plt.legend(frameon=False)

for year, subset in data.groupby('year'):
    print year, subset[subset.score == subset.score.max()].title.values

Explore the data on your own using Pandas. 
At the bottom of your script, write out (as comments) 
two interesting facts that you learned about the data, 
and show the code you used to find those facts.

Comments: So, in the data wrangling examples above, 
it looks like movies with large amounts of votes 
tend to have higher scores, so I'd like to use OLS
 regression to see if the number of votes can be
 used to predict the score.
 
from pandas.stats.api import ols
df = pd.read_csv('https://raw.githubusercontent.com/cs109/content/master/imdb_top_10000.txt', delimiter='\t', names=names).dropna()
res = ols(y=df['score'], x=df['votes'])
res

-------------------------Summary of Regression Analysis-------------------------

Formula: Y ~ <x> + <intercept>

Number of Observations:         9999
Number of Degrees of Freedom:   2

R-squared:         0.0708
Adj R-squared:     0.0707

Rmse:              1.1472

F-stat (1, 9997):   761.1442, p-value:     0.0000

Degrees of Freedom: model 1, resid 9997

-----------------------Summary of Estimated Coefficients------------------------
      Variable       Coef    Std Err     t-stat    p-value    CI 2.5%   CI 97.5%
--------------------------------------------------------------------------------
             x     0.0000     0.0000      27.59     0.0000     0.0000     0.0000
     intercept     6.2339     0.0127     489.80     0.0000     6.2090     6.2589
---------------------------------End of Summary---------------------------------

Comments: Ok, so the R-squared value doesn't suggest there is a good fit here.
 
Now, let's see what happens if we add another attribute - runtime.

from pandas.stats.api import ols
df = pd.read_csv('https://raw.githubusercontent.com/cs109/content/master/imdb_top_10000.txt', delimiter='\t', names=names).dropna()
clean_runtime = [float(r.split(' ')[0]) for r in df.runtime]
df['runtime'] = clean_runtime
res = ols(y=df['score'], x=df[['votes', 'runtime']]) 
res

-------------------------Summary of Regression Analysis-------------------------

Formula: Y ~ <votes> + <runtime> + <intercept>

Number of Observations:         9999
Number of Degrees of Freedom:   3

R-squared:         0.1121
Adj R-squared:     0.1119

Rmse:              1.1214

F-stat (2, 9996):   630.8065, p-value:     0.0000

Degrees of Freedom: model 2, resid 9996

-----------------------Summary of Estimated Coefficients------------------------
      Variable       Coef    Std Err     t-stat    p-value    CI 2.5%   CI 97.5%
--------------------------------------------------------------------------------
         votes     0.0000     0.0000      23.38     0.0000     0.0000     0.0000
       runtime     0.0093     0.0004      21.57     0.0000     0.0084     0.0101
     intercept     5.2975     0.0452     117.29     0.0000     5.2090     5.3860
---------------------------------End of Summary---------------------------------

Hmm, neither attribute seems to be a great predictor of score.

Let's make a scatter-plot and see the data visualized - 

plt.scatter(data.votes, data.score, alpha=.04, lw=0, color='k')
plt.xlabel("votes")
plt.ylabel("score")
plt.legend(frameon=False)

There's an almost logarithmic curve apparent - but obviously not much of a line.
There does seem to be a phenomenon whereby a lot of people log on to eagerly rate movies they like 
- or maybe even a bandwagoning effect, perhaps? 

I wonder if the mean score varies by genre?

genre_mean = data.groupby(genre).score.mean()
genre_mean.name = 'Genre Mean'
print genre_mean

Q: Why am I only getting Western?

plt.plot(genre_mean.index, genre_mean.values, 'o-',
        color='r', lw=3, label='Genre Average')
        
data.plt(kind='bar')
(data.genre, data.genre_mean, alpha=.04, lw=0, color='k')
plt.xlabel("genre")
plt.ylabel("genre_mean")
plt.legend(frameon=False)

Ok, I tried to figure this out - I know I need to do something where I take all the 
films for which western=true, and get the mean that way, but I've run out of time!
















