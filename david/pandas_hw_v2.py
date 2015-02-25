#%matplotlib inline

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#tell pandas to display wide tables as pretty HTML tables
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)

names = ['imdbID', 'title', 'year', 'score', 'votes', 'runtime', 'genres']
data = pd.read_csv('https://raw.githubusercontent.com/cs109/content/master/imdb_top_10000.txt', delimiter='\t', names=names).dropna(how='all').dropna()

#print "Number of rows: %i" % data.shape[0], "\n\n"
#clean the runtime in the dataframe
clean_runtime = [float(r.split(' ')[0]) for r in data.runtime]
data['runtime'] = clean_runtime

#probably best to flag those bad data as NAN
data.runtime[data.runtime==0] = np.nan

#determine the unique genres
genres = set()
for m in data.genres:
    genres.update(g for g in str(m).split('|'))
genres = sorted(genres)

#make a column for each genre
for genre in genres:
    data[genre] = [genre in movie.split('|') for movie in data.genres]
    #how does the above create a boolean flag for each cell in the view?
    #loops over each movie in top 10000
    #loops over the set() of genres and marks true if any genre is in the genres.split('|')

#remove year from the movie name column
data['title'] = [t[0:-7] for t in data.title]
print data.head()

#mean score for all movies in each decade
decade =  (data.year // 10) * 10
decade_mean = data.groupby(decade).runtime.mean()
decade_median = data.groupby(decade).runtime.median()
decade_mean.name = 'Decade Mean'
decade_median.name = 'Decade Median'
print decade_mean

#plot runtime by year
grouped_runtime = data.groupby(decade).runtime
mean = grouped_runtime.mean()
median = grouped_runtime.median()
std = grouped_runtime.std()

#plotting inputs
#plot the median runtime of movies by decade
plt.plot(decade_median.index, decade_median.values, 'o-',
        color='r', lw=3, label='Decade Average')
plt.fill_between(decade_median.index, (decade_median + std).values,
                (decade_median - std).values, color='r', alpha=.2)
plt.scatter(data.year, data.runtime, alpha=.04, lw=0, color='k')
plt.xlabel("Year")
plt.ylabel("Runtime")
plt.legend(frameon=False)
plt.show()

'''
Kevin Markham [8:54 PM]
`data.year.value_counts()` shows me how many records there were for each year

the other way to accomplish this is: `data.groupby('year').year.count()`

In other words, `value_counts()` is a convenience method for a groupby AND selection of column AND count

thus, you would tend not to put `value_counts()` in a statement that includes a `groupby`

so, you probably want something more like this: `data[data.runtime > 120].groupby('year').runtime.count()`

and then for the plot, you probably want a bar plot: `data[data.runtime > 120].groupby('year').runtime.count().plot(kind='bar')`
'''
#plot the frequency count of movies over 120 minutes by year
data[data.runtime > 120].groupby('year').runtime.count().plot(kind='line', label='Movies Over 120 Minutes')
plt.xlabel("Year")
plt.ylabel("Count of Movies over 120 Minutes")
plt.show()

#plot the frequency count of movies under 90 minutes by year
data[data.runtime < 90].groupby('year').runtime.count().plot(kind='line', label='Movies Under 90 Minutes')
plt.xlabel("Year")
plt.ylabel("Count of Movies under 90 Minutes")
plt.show()

#plot standard deviation of movie runtime by year
runtime_std = data.groupby('year').runtime.std()
plt.xlabel("Year")
plt.ylabel("STD of Runtime")
runtime_std.plot(kind='bar')
plt.show()

#1: the median and mean runtime of movies has not increased much over time
#2: the standard deviation of movie runtime has decreased from previous peaks, but the frequency of longer runtimes is increasing.
#3: I was unable to figure out how to plot the % of movies over 120 or under 90, which would have normalized for number of movies released
#I submitted several charts. One showing frequency of movies over 120, one showing frequency of movies under 90, one showing the median runtime by decade
#and another showing the standard deviation in runtime by year.
