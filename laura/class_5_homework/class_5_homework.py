# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 19:12:25 2015

@author: laura
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#tell pandas to display wide tables as pretty HTML tables
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)


  
names = ['imdbID', 'title', 'year', 'score', 'votes', 'runtime', 'genres']
data = pd.read_csv('data/imdb_top_10000.txt', delimiter='\t', names=names).dropna()
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

plt.hist(data.score, bins=20, color='#cccccc')
plt.xlabel("IMDB rating")

plt.hist(data.runtime.dropna(), bins=50, color='#cccccc')
plt.xlabel("Runtime distribution")


#hmm, more bad, recent movies. Real, or a selection bias?
plt.scatter(data.year, data.score, lw=0, alpha=.08, color='k')
plt.xlabel("Year")
plt.ylabel("IMDB Rating")

plt.scatter(data.votes, data.score, lw=0, alpha=.2, color='k')
plt.xlabel("Number of Votes")
plt.ylabel("IMDB Rating")
plt.xscale('log')

# low-score movies with lots of votes
data[(data.votes > 9e4) & (data.score < 5)][['title', 'year', 'score', 'votes', 'genres']]

# The lowest rated movies
data[data.score == data.score.min()][['title', 'year', 'score', 'votes', 'genres']]

# The highest rated movies
data[data.score == data.score.max()][['title', 'year', 'score', 'votes', 'genres']]

# QUESTION: why doesn't this show the genre names for me?
#sum sums over rows by default
data[genres].sum()
genre_count = np.sort(data[genres].sum())[::-1]
pd.DataFrame({'Genre Count': genre_count})

#axis=1 sums over columns instead
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
    
#THIS DID NOT WORK
#create a 4x6 grid of plots.
fig, axes = plt.subplots(nrows=4, ncols=6, figsize=(12, 8), 
                         tight_layout=True)

bins = np.arange(1950, 2013, 3)
for ax, genre in zip(axes.ravel(), genres):
    ax.hist(data[data[genre] == 1].year, 
            bins=bins, histtype='stepfilled', normed=True, color='r', alpha=.3, ec='none')
    ax.hist(data.year, bins=bins, histtype='stepfilled', ec='None', normed=True, zorder=0, color='#cccccc')
    
    ax.annotate(genre, xy=(1955, 3e-2), fontsize=14)
    ax.xaxis.set_ticks(np.arange(1950, 2013, 30))
    ax.set_yticks([])
    #remove_border(ax, left=False)
    ax.set_xlabel('Year')

#THIS DID NOT WORK
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
    #remove_border(ax, left=False)
    ax.annotate(genre, xy=(230, .02), ha='right', fontsize=12)
 
#THIS DID NOT WORK   
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
    #remove_border(ax, left=False)
    ax.set_ylim(0, .4)
    ax.annotate(genre, xy=(0, .2), ha='left', fontsize=12)
    
    
    
    
    
    
    
    
    
######  Additional exploration / plots ######
    
    
'''
Does the length of the title effect the average score?  
Answer: No
'''

# scatterplot of title length v. score
data.plot(kind='scatter', x='title_length', y='score', alpha=0.3)
plt.savefig('score_titlelength.png')

    
    
    
'''
Have movie titles become shorter or longer over the years? 
Answer: Slightly shorter
'''
# scatterplot of year v. title_length with average 
title_length_mean = data.groupby(decade).title_length.mean()
title_length_mean.name = 'Title Length Mean'
print title_length_mean

plt.plot(title_length_mean.index, title_length_mean.values, 'o-',
        color='r', lw=3, label='Title Length Average')
plt.scatter(data.year, data.title_length, alpha=.04, lw=0, color='k')
plt.xlabel("Year")
plt.ylabel("Title Length")
plt.legend(frameon=False)
plt.savefig('titlelength_by_year.png')




'''
What are the longest and shortest movies in this data?
'''
# The longest 5 movies
data.sort_index(by='runtime', ascending=False).head(5)[['title', 'year', 'score', 'runtime']]

# The shortest 5 movies
data.sort_index(by='runtime').head(5)[['title', 'year', 'score', 'runtime']]




'''
Has average runtime become shorter or longer over the years?  
Answer: no overall trend, but we did have longer movies in the 60s and 70s
'''

runtime_mean = data.groupby(decade).runtime.mean()
runtime_mean.name = 'Runtime Mean'
print runtime_mean

plt.plot(runtime_mean.index, runtime_mean.values, 'o-',
        color='r', lw=3, label='Runtime Average')
plt.scatter(data.year, data.runtime, alpha=.04, lw=0, color='k')
plt.xlabel("Year")
plt.ylabel("Runtime")
plt.legend(frameon=False)
plt.savefig('runtime_by_year.png')


'''
Does the runtime effect the score?  Nope.
'''

# scatterplot of runtime v. score with average
score_mean = data.groupby('runtime').score.mean()
plt.plot(score_mean.index, score_mean.values, 'o-',
        color='r', lw=3, label='Score Average')
plt.scatter(data.runtime, data.score, alpha=.04, lw=0, color='k')
plt.xlabel("Runtime")
plt.ylabel("Score")
plt.legend(frameon=False)
plt.savefig('runtime_score_v1.png')

'''
The last chart is interesting, but outliers are throwing making it hard to view!  

Two ideas to explore: 
   1) look at a narrow range (drop the outliers)  
   2) smooth out graph by taking averages
   
'''

# look at a narrow range (drop the outliers)
data_range = data[(data.runtime < 200) & (data.runtime > 70)] 
score_mean = data_range.groupby('runtime').score.mean()
plt.plot(score_mean.index, score_mean.values, 'o-',
        color='r', lw=3, label='Score Average')
plt.scatter(data_range.runtime, data_range.score, alpha=.04, lw=0, color='k')
plt.xlabel("Runtime")
plt.ylabel("Score")
plt.legend(frameon=False)
plt.savefig('runtime_score_v2.png')


# smooth out graph by taking averages
runtime_group =  (data.runtime // 10) * 10
runtime_group.value_counts()
score_mean = data.groupby(runtime_group).score.mean()
plt.plot(score_mean.index, score_mean.values, 'o-',
        color='r', lw=3, label='Score Average')
plt.scatter(data_range.runtime, data_range.score, alpha=.04, lw=0, color='k')
plt.xlabel("Runtime")
plt.ylabel("Score")
plt.legend(frameon=False)
plt.savefig('runtime_score_v3.png')
