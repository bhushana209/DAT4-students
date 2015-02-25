# -*- coding: utf-8 -*-
"""
Pandas homework (from class 5)
Created on Mon Jan 12 10:53:08 2015

@author: abrown1

after the copied code, I tried two questions:
1: are longer movies better?
2: what genres tend to be co-labelled?

"""

# Block 1

# import the relevant libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.api as sm
import heapq

#tell pandas to display wide tables as pretty HTML tables
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)

def remove_border(axes=None, top=False, right=False, left=True, bottom=True):
    """
    Minimize chartjunk by stripping out unnecesasry plot borders and axis ticks
    
    The top/right/left/bottom keywords toggle whether the corresponding plot border is drawn
    """
    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)
    
    #turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')
    
    #now re-enable visibles
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()
        
# block2: sets up some column names. Then reads the txt and uses the names as names
names = ['imdbID', 'title', 'year', 'score', 'votes', 'runtime', 'genres']
data = pd.read_csv('imdb_top_10000.txt', delimiter='\t', names=names).dropna()
print "Number of rows: %i" % data.shape[0]
data.head()  # print the first 5 rows 

# block 3 (skipped a demo snippet) - uses list comprehension to turn all the run times into real numbers
clean_runtime = [float(r.split(' ')[0]) for r in data.runtime]
data['runtime'] = clean_runtime
data.head()

# block 4: looks through to identify all the unique genres, makes a "matrix" (heh)
# of each then sets true for a movie if it is tagged that genre
#determine the unique genres
genres = set()
for m in data.genres:
    genres.update(g for g in m.split('|'))
genres = sorted(genres)

#make a column for each genre
for genre in genres:
    data[genre] = [genre in movie.split('|') for movie in data.genres]
         
data.head()

# block 5: remove the (year) frome the title since it's in the data column
data['title'] = [t[0:-7] for t in data.title]
data.head()

# describe each column
data[['score', 'runtime', 'year', 'votes']].describe()

# identify and remove the 0 runtime movies
#hmmm, a runtime of 0 looks suspicious. How many movies have that?
print len(data[data.runtime == 0])

#probably best to flag those bad data as NAN
data.runtime[data.runtime==0] = np.nan
# min is now 45

# plotting blocks
# more movies in recent years, but not *very* recent movies (they haven't had time to receive lots of votes yet?)
plt.hist(data.year, bins=np.arange(1950, 2013), color='#cccccc')
plt.xlabel("Release Year")
remove_border()

# ratings are non-gaussian - the are longer-tailed to the lower raitings, and very few with very high averages.
plt.hist(data.score, bins=20, color='#cccccc')
plt.xlabel("IMDB rating")
remove_border()

#lengths are also non-gaussian, with longer tail to long movies.
plt.hist(data.runtime.dropna(), bins=50, color='#cccccc')
plt.xlabel("Runtime distribution")
remove_border()

#hmm, more bad, recent movies. Real, or a selection bias?

plt.scatter(data.year, data.score, lw=0, alpha=.08, color='k')
plt.xlabel("Year")
plt.ylabel("IMDB Rating")
remove_border()

# better movies tend to have more votes, or at least bad movies don't have a lot
plt.scatter(data.votes, data.score, lw=0, alpha=.2, color='k')
plt.xlabel("Number of Votes")
plt.ylabel("IMDB Rating")
plt.xscale('log')
remove_border()

# low-score movies with lots of votes
data[(data.votes > 9e4) & (data.score < 6)][['title', 'year', 'score', 'votes', 'genres']]

# The lowest rated movies
data[data.score == data.score.min()][['title', 'year', 'score', 'votes', 'genres']]

# The highest rated movies
data[data.score == data.score.max()][['title', 'year', 'score', 'votes', 'genres']]

# counts genres
#sum sums over rows by default
genre_count = np.sort(data[genres].sum())[::-1]
pd.DataFrame({'Genre Count': genre_count})

# how many genres does the average movie have?
#axis=1 sums over columns instead
genre_count = data[genres].sum(axis=1) 
print "Average movie has %0.2f genres" % genre_count.mean()
genre_count.describe()

# make decades and group by decade into 'tyd'
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
remove_border()

# now also add scatter by year, with a standard deviation for each year as a band
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
remove_border()

# print the highest-rated movie in each year
for year, subset in data.groupby('year'):
    print year, subset[subset.score == subset.score.max()].title.values

#compare the frequency of each genre over time
#create a 4x6 grid of plots.
fig, axes = plt.subplots(nrows=4, ncols=6, figsize=(12, 8), 
                         tight_layout=True)

bins = np.arange(1950, 2013, 3)
# for each genre
for ax, genre in zip(axes.ravel(), genres):
    ax.hist(data[data[genre] == 1].year, 
            bins=bins, histtype='stepfilled', normed=True, color='r', alpha=.3, ec='none')
    ax.hist(data.year, bins=bins, histtype='stepfilled', ec='None', normed=True, zorder=0, color='#cccccc')
    
    ax.annotate(genre, xy=(1955, 3e-2), fontsize=14)
    ax.xaxis.set_ticks(np.arange(1950, 2013, 30))
    ax.set_yticks([])
    remove_border(ax, left=False)
    ax.set_xlabel('Year')
    
# look at runtime distributions by genre
fig, axes = plt.subplots(nrows=4, ncols=6, figsize=(12, 8), tight_layout=True)

bins = np.arange(30, 240, 10)

for ax, genre in zip(axes.ravel(), genres):
    ax.hist(data[data[genre] == 1].runtime, 
            bins=bins, histtype='stepfilled', color='r', ec='none', alpha=.3, normed=True)
               
    ax.hist(data.runtime, bins=bins, normed=True,
            histtype='stepfilled', ec='none', color='#cccccc',
            zorder=0)
    
    ax.set_xticks(np.arange(30, 240, 60))
    ax.set_yticks([])
    ax.set_xlabel("Runtime [min]")
    remove_border(ax, left=False)
    ax.annotate(genre, xy=(230, .02), ha='right', fontsize=12)    

# look at rating distribution by genre
fig, axes = plt.subplots(nrows=4, ncols=6, figsize=(12, 8), tight_layout=True)

bins = np.arange(0, 10, .5)

for ax, genre in zip(axes.ravel(), genres):
    ax.hist(data[data[genre] == 1].score, 
            bins=bins, histtype='stepfilled', color='r', ec='none', alpha=.3, normed=True)
               
    ax.hist(data.score, bins=bins, normed=True,
            histtype='stepfilled', ec='none', color='#cccccc',
            zorder=0)
    
    ax.set_yticks([])
    ax.set_xlabel("Score")
    remove_border(ax, left=False)
    ax.set_ylim(0, .4)
    ax.annotate(genre, xy=(0, .2), ha='left', fontsize=12)

""" Homework response section:


Fact 1: mostly, better movies have more votes. We identified some outliers, and found that people love to hate (and vote agains) twilight movies.
I identified this with the code for the worst movies with the most votes, but increased the score threshold to 6
>>> low-score movies with lots of votes
>>> data[(data.votes > 9e4) & (data.score < 6)][['title', 'year', 'score', 'votes', 'genres']]

Images: Are better movies longer?

How have movie lengths changed over time?

What genres frequently occur together?

"""

# Are better movies longer? Adapt the split by year to split by length
# set the scale to exclude some very, very long movies
plt.scatter(data.runtime, data.score, lw=0, alpha=.08, color='k')
plt.xlabel("Run Time")
plt.ylabel("IMDB Rating")
# plt.set_xlim(0, 250)
remove_border()

#Fact2: above - there are barely any short, low-rated movies. There are good short movies, bad short movies, but pretty few long, bad movies
# it's possible that they only make long movies if they will be good, or that people stop watching crappy long movies and don't rate them!

#What genres frequently occur together?
#make a gxg (where g is number of genres) where each cell is the likelihood that if g1 is true, g2 is true
# or maybe I want to normalize by p_g2 to avoide biasing by absolute frequency of the genre?

# first, use an inner product with the genres. This shoudl give the cross-count in each cell. The diagnol is the total for each genre if I want to normalize
g_corr = np.inner(data[genres].astype(float).T,data[genres].astype(float).T)
g_diag = g_corr.diagonal().copy()
# since I don't want the diagnol messing up maxes, etc., fill the diagnol with zeros
np.fill_diagonal(g_corr, 0)

# tried this unnormalized - but the stongest cells are jsut the common genre.

#normalize by the total number of movies that have that genre. That is, calc a normalized corrolation that is:
# intersect(g1, g2) / union (g1, g2). In practices, intersect is the g_corr matrix and union is the just the total in both genres
# which I can grab from the diagnols stored.
g_corr_norm = g_corr.copy()
for n in range(0,len(genres)):
    for m in range(0,len(genres)):
        g_corr_norm[n][m] = g_corr[n][m] / (g_diag[n]+g_diag[m])

# plot the matrix with the genres as names
sm.graphics.plot_corr(g_corr_norm, xnames = genres)
# find the top ten values - note I skip every other value 
g_corr_norm_find = g_corr_norm.copy()
g_corr_norm_find = g_corr_norm_find.flatten()
g_corr_norm_find.sort()
top_vals = list(range(10))
for n in range(10):
    top_vals[n] = g_corr_norm_find[-2*n-1]
for val in top_vals:
    [(i,j) for i,x in enumerate(g_corr_norm) for j,y in enumerate(x) if y == val]


"""
ok! This works *great*. Visually, I notice:
several genres - news, reality, and adult - are never (or extremely rarely) conamed with another genre
the strongest cells are:
1: crime - thriller
2: comedy - romance
3: drama - romance
4: animation - family
5: action - thriller
6: action - adventure
7: adventure - family
8: mystery - thriller
9: drama - thriller
10: thriller - horror

graphic 2 is the result of this plot.
the find code results in :

[(6, 21), (21, 6)]
[(5, 18), (18, 5)]
[(7, 18), (18, 7)]
[(3, 8), (8, 3)]
[(0, 21), (21, 0)]
[(0, 2), (2, 0)]
[(2, 8), (8, 2)]
[(15, 21), (21, 15)]
[(7, 21), (21, 7)]
[(12, 21), (21, 12)]
"""
