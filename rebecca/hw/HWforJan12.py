# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 11:02:54 2015

@author: rdecrescenzo
"""



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

pd.read_table("https://raw.githubusercontent.com/cs109/content/master/imdb_top_10000.txt")

names = ['imdbID','title', 'year','score','votes','runtime','genres']
data = pd.read_csv("https://raw.githubusercontent.com/cs109/content/master/imdb_top_10000.txt",delimiter='\t', names=names).dropna()
print 'Number of rows: %i' % data.shape[0]
data.head()

dirty = '142 mins.'
number, text = dirty.split(' ')
clean = int(number)
print number

clean_runtime = [float(r.split(' ')[0]) for r in data.runtime]
data['runtime'] = clean_runtime
data.head()

genres = set()
for m in data.genres:
    genres.update(g for g in m.split('|'))
genres = sorted(genres)

for genre in genres:
    data[genre] = [genre in movie.split('|') for movie in data.genres]
    
data.head()

data['title'] = [t[0:-7] for t in data.title]
data.head()

data[['score','runtime','year','votes']].describe()

print len(data[data.runtime == 0])
data.runtime[data.runtime == 0] = np.nan

data.runtime.describe()

plt.hist(data.year, bins=np.arange(1950, 2013), color='#cccccc')
plt.xlabel("Release Year")

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

data[(data.votes > 9e4) & (data.score < 5)][['title', 'year', 'score', 'votes', 'genres']]

data[data.score == data.score.min()][['title', 'year', 'score', 'votes', 'genres']]

data[data.score == data.score.max()][['title', 'year', 'score', 'votes', 'genres']]

genre_count = np.sort(data[genres].sum())[::-1]
pd.DataFrame({'Genre Count': genre_count})

genre_count = data[genres].sum(axis=1) 
print "Average movie has %0.2f genres" % genre_count.mean()
genre_count.describe()

decade =  (data.year // 10) * 10

tyd = data[['title', 'year']]
tyd['decade'] = decade

tyd.head()

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
    
#Plot A
#I wanted to see if there was a possible runtime/score correlation
runtime_bucket =  (data.runtime // 10) * 10


runtime_mean = data.groupby(runtime_bucket).score.mean()
runtime_mean.name = 'Runtime Mean'
print runtime_mean

plt.plot(runtime_mean.index, runtime_mean.values, 'o-',
    color='r', lw=1, label='Runtime Average')
plt.scatter(data.runtime, data.score, alpha=.06, lw=0, color='k')
plt.xlabel("Runtime distribution")
plt.ylabel("IMDB Rating")
plt.legend(frameon=False)
#Interesting
#Basically, it would appear prima facia that if you would like to see a movie that is highly rated on IMDB, then you would most likely wish to see a movie that is over 100 minutes long
#Until the movie begins to approach 200 minutes, in which case the amount of movies review drops
#My guess would be that long movies are a. boring (even if critically acclaimed), b. expensive to make, c. box-office flops
#But you really are best off seeing a movie that's 130-220 minutes long if IMDB ratings are your homeboys
#However, if you truly want to see a good movie, you should probably just listen to my suggstions hahaha
#JK (sort of, although a personal friend is typically better than strangers when choosing a movie)

#Checking to see how it looks the other way
imdb_rating =  (data.score)


rating_mean = data.groupby('score').runtime.mean()
rating_mean.name = 'Rating Mean'
print rating_mean

plt.plot(rating_mean.index, rating_mean.values, 'o-',
    color='r', lw=1, label='Rating Average')
plt.scatter(data.score, data.runtime, alpha=.06, lw=0, color='k')
plt.xlabel("IMDB Rating Distribution")
plt.ylabel("Runtime")
plt.legend(frameon=False)
#can see the runtimes go up a bit with rating, however does not appear that rating is the independent variable 

#Looking for the ratings outliers that showed up in Plot A
#Looking for excellently rated short films
data[(data.runtime < 60) & (data.score > 6)][['title', 'year', 'score', 'votes', 'genres']]

#Looking for long, shitty movies
data[(data.runtime > 150) & (data.score < 6)][['title', 'year', 'score', 'votes', 'genres']]

plt.hist(((data.runtime > 150) & (data.score < 6)).dropna(), bins=4, color='#cccccc')
plt.xlabel("Woah These Movies are Long and Boring")

#Looking to see how many votes were going on by year

what_year_isit =  (data.year)


voting_mean = data.groupby('year').votes.mean()
voting_mean.name = 'Year Mean'
print voting_mean

plt.plot(voting_mean.index, voting_mean.values, 'o-',
    color='r', lw=1, label='Voting Average')
    
plt.scatter(data.year, (data.votes < 300000), alpha=.01, lw=0, color='k')
plt.xlabel("Year")
plt.ylabel("# Votes")
plt.legend(frameon=False)

#It appears that the #votes are going up by the year
#That would suggest that either IMDB is growing more popular or the internet and/or movies are becoming more popular and IMDB is riding the wave
#Most likely the internet is becoming larger and IMDB is still a relatively popular channel for movie ratings
#Although if you look at that drop from 2010-11 # Disruption Town! Resident: IMDB
