# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 13:07:59 2015

@author: Jason
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

names = ['imdbID', 'title', 'year', 'score', 'votes', 'runtime', 'genres']
data = pd.read_csv('/Users/Jason/Documents/DataScience/DAT4-students/jason/data/imdb_top_10000.txt', 
                   delimiter = '\t', names = names).dropna()
print "Number of rows: %i" % data.shape[0]
data.head()

dirty = '142 mins.'
number, text = dirty.split(' ')
clean = int(number)
print number

# clean the runtime column
clean_runtime = [float(r.split(' ')[0]) for r in data.runtime]
data['runtime'] = clean_runtime
data.head()

#clean and split the genres
genres = set()
for m in data.genres:
    genres.update(g for g in m.split('|'))
genres = sorted(genres)

for genre in genres:
    data[genre] = [genre in movie.split('|') for movie in data.genres]

data.head()

# strip years out of movie titles
data['title'] = [t[0:-7] for t in data.title]
data.head()

data[['score', 'runtime', 'year', 'votes']].describe()

print len(data[data.runtime == 0])
data.runtime[data.runtime == 0] = np.nan

data.runtime.describe()

plt.hist(data.year, bins = np.arange(1950, 2013), color = '#cccccc')
# data.year.hist(bins = 62)
plt.xlabel("Release Year")

data.score.hist(bins = 20)
plt.xlabel("IMDB rating")

data.runtime.dropna().hist(bins = 50)
plt.xlabel("Runtime distribution")

plt.scatter(data.year, data.score, lw = 0, alpha = .08, color = 'k')
plt.xlabel("Year")
plt.ylabel("IMDB rating")

plt.scatter(data.votes, data.score, lw = 0, alpha = .2, color = 'k')
plt.xlabel("Number of votes")
plt.ylabel("IMDB Rating")
plt.xscale('log')

data[(data.votes > 9e4) & (data.score < 5)][['title', 'year', 'score', 'votes', 'genres']]

data[data.score == data.score.min()][['title', 'year', 'score', 'votes', 'genres']]

data[data.score == data.score.max()][['title', 'year', 'score', 'votes', 'genres']]

genre_count = np.sort(data[genres].sum())[::-1]
pd.DataFrame({'Genre Count': genre_count})

genre_count = data[genres].sum(axis = 1)
print "Average movie has %0.2f genres" % genre_count.mean()
genre_count.describe()

decade = (data.year // 10) * 10

tyd = data[['title', 'year']]
tyd['decade'] = decade

tyd.head()

decade_mean = data.groupby(decade).score.mean()
decade_mean.name = "Decade Mean"
print decade_mean

plt.plot(decade_mean.index, decade_mean.values, 'o-',
         color = 'r', lw = 3, label = 'Decade Averages')
plt.scatter(data.year, data.score, alpha = .04, lw = 0, color = 'k')
plt.xlabel("Year")
plt.ylabel("Score")
plt.legend(frameon = False)

grouped_scores = data.groupby(decade).score
mean = grouped_scores.mean()
std = grouped_scores.std()

plt.plot(decade_mean.index, decade_mean.values, 'o-',
         color = 'r', lw = 3, label = "Decade Average")
plt.fill_between(decade_mean.index, (decade_mean + std).values,
                 (decade_mean - std).values, color = 'r', alpha = .2)
plt.scatter(data.year, data.score, alpha = .04, lw = 0, color = 'k')
plt.xlabel('Year')
plt.ylabel('Score')
plt.legend(frameon = False)

for year, subset in data.groupby('year'):
    print year, subset[subset.score == subset.score.max()].title.values

# Jason's homework section

data.plot(kind = 'scatter', x = 'runtime', y = 'score', alpha = 0.3)
'''
Observation 1: At first glance, there doesn't seem to be a strong correlation 
between a movie's length and its score.
'''

grouped_runtimes = data.groupby(decade).runtime
runtime_mean = grouped_runtimes.mean()
runtime_mean.name = "Decade Runtime Mean"
run_std = grouped_runtimes.std()

plt.plot(runtime_mean.index, runtime_mean.values, 'o-',
         color = 'r', lw = 3, label = "Decade Runtime Average")
plt.fill_between(runtime_mean.index, (runtime_mean + run_std).values, 
                 (runtime_mean - run_std).values, color = 'r', alpha = .2)
plt.scatter(data.year, data.runtime, alpha = 0.01, lw = 0, color = 'k')
plt.xlabel('Year')
plt.ylabel('Runtime')
plt.ylim(0, 300)
plt.legend(frameon = False)
'''
Observation 2: While the average length of movies has remained relatively constant,
the standard deviation has observably decreased since the 1960s.
'''