import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

names = ['imdbID', 'title', 'year', 'score', 'votes', 'runtime', 'genres']
imdb_data_url = 'https://raw.githubusercontent.com/cs109/content/master/imdb_top_10000.txt'
data = pd.read_csv(imdb_data_url, delimiter='\t', names=names).dropna()
print "Number of rows: %i" % data.shape[0]
data.head()  # print the first 5 rows

 
# Clean the DataFrame

dirty = '142 mins.' # the original string
number, text = dirty.split(' ') # split into new values named object and number on the space
clean = int(number) # define the clean value as an integer
print number

clean_runtime = [float(r.split(' ')[0]) for r in data.runtime]
data.runtime = clean_runtime
data.head()

#determine the unique genres

genres = set() # set is like a list, but will not contain duplicate values

for m in data.genres:
    genres.update(g for g in m.split('|')) # why update and not append?

genres = sorted(genres)

#Make a column for each genre

for genre in genres:
    data[genre] = [genre in movie.split('|') for movie in data.genres]    

# this for loop creates a column labeled as a genre from the genres set
# the list comprehension takes the movie type which is not yet split up
# from the genres column in the dataframe, the split method is then applied
# to movie and the in function is used to compare genre from the genres set
# to the list of movie genres created by the split.  The columns are populated
# with True or False    


data.head()


# Remove year from Title
data.title = [title[:-7] for title in data.title]


# 3. Explore global properties
data.dtypes
data_integers = ['year', 'score', 'votes', 'runtime']
data[data_integers].describe()

# check out the minimum value of runtime.  0 isn't feasible
# How many movies have a 0 runtime?

print len(data[data.runtime == 0])
#probably best to flag those bad data as NAN

data.runtime[data.runtime == 0] = np.nan

# check the runtime summary again....
data.runtime.describe()


# Histograms

# more movies in recent years, but not *very* recent movies (they haven't had time to receive lots of votes yet?)
plt.hist(data.year, bins=np.arange(1950, 2013), color='#cccccc')
plt.xlabel("Release Year")



plt.hist(data.score, bins=20, color='#cccccc')
plt.xlabel("IMDB rating")

plt.hist(data.runtime.dropna(), bins = 50, color='#cccccc')
plt.xlabel("Runtime Distribution")

# Scatter Plots
##hmm, more bad, recent movies. Real, or a selection bias?

plt.scatter(data.year, data.score, lw=0, alpha = .08, color='k')
plt.xlabel("Year")
plt.ylabel("IMDB Rating")

plt.scatter(data.votes, data.score, lw=0, alpha=.2, color='k')
plt.xlabel("Number of Votes")
plt.ylabel("IMDB Rating")
plt.xscale('log')

# Identify some outliers
# Low-score movies with lots of votes
data[(data.votes > 9e4) & (data.score < 5)][['title', 'year', 'score', 'votes', 'genres']]

# The Lowest rated movies
data[(data.score == data.score.min())][['title', 'year', 'score', 'votes', 'genres']]

# The highest rated movies
data[(data.score == data.score.max())][['title', 'year', 'score', 'votes', 'genres']]

# Run aggregation function like sum over several rowws or columns
# What genres are the most frequent

# sum sums over rows by default
genre_count = np.sort(data[genres].sum())[::-1] # this slice puts the list in descending order
pd.DataFrame({'Genre Count' : genre_count})


# How many genres does a movie have, on average?


#axis=1 sums over columns instead

# Note axis one sums in the horizontal direction
genre_count = data[genres].sum(axis=1) 
print "Average movie has %0.2f genres" % genre_count.mean()
genre_count.describe()

# Explore group properties, split movies by decade

# this is way more efficient than what I would have tried!

decade = (data.year // 10) * 10 #floor division to divide years by 10 and remove the tenths column of the result

tyd = data[['title', 'year']]
tyd['decade'] = decade

tyd.head()

# GroupBy will gather movies into groups with equal decade values
# mean score for all movies in each decade

decade_mean = data.groupby(decade).score.mean()
decade_mean.name = 'Decade Mean'
print decade_mean

plt.plot(decade_mean.index, decade_mean.values, 'o-', color = 'r', lw =3, label = 'Decade Average')
plt.scatter(data.year, data.score, alpha=.04, lw=0, color = 'k')
plt.xlabel('Year')
plt.ylabel('Score')
plt.legend(frameon = False)

# We can go one step further, and compute the scatter in each year as well
# use the built in standard deviation function std()
grouped_scores = data.groupby(decade).score
std = grouped_scores.std() # get the standard deviation in scores at each decade

plt.plot(decade_mean.index, decade_mean.values, 'o-',
        color='r', lw=3, label='Decade Average')

# fill_between used to color the region one std above and below the mean
plt.fill_between(decade_mean.index, (decade_mean + std).values,
                 (decade_mean - std).values, color='r', alpha=.2)
plt.scatter(data.year, data.score, alpha=.04, lw=0, color='k')
plt.xlabel("Year")
plt.ylabel("Score")
plt.legend(frameon=False)

'''You can also iterate over a GroupBy object. Each iteration yields two 
variables: one of the distinct values of the group key, and the subset of 
the dataframe where the key equals that value. To find the most popular movie 
each year: '''


for year, subset in data.groupby('year'):
    print year, subset[subset.score == subset.score.max()].title.values

'''Small multiples
Let's split up the movies by genre, and look at how their release 
year/runtime/IMDB score vary. The distribution for all movies is shown as a 
grey background.

This isn't a standard groupby, so we can't use the groupby method here.
A manual loop is needed  '''  
    
    
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
    ax.set_xlabel('Year')
    
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
    ax.annotate(genre, xy=(230, .02), ha='right', fontsize=12)
    
    
    
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
    ax.set_ylim(0, .4)
    ax.annotate(genre, xy=(0, .2), ha='left', fontsize=12)

###############################################################################

# Has the runtime of movies changed with time? Not really, but we could alreqdy
# infer that from the previous histogram.

plt.scatter(data.year, data.runtime, lw=0, alpha = .08, color='red')
plt.xlabel("Year")
plt.ylabel("Runtime (minutes)")
plt.annotate('War and Peace', (1967, 427))
plt.annotate('Satantango', (1994, 450))


# There are a few outliers, what are they?

data[data.runtime > 400][['title', 'year', 'runtime']]


# Do people give "longer" movies an above average score?
plt.scatter(data.runtime, data.score, lw=0, alpha = .08)
plt.xlabel('Runtime (minutes)')
plt.ylabel('Score')

data[data.runtime < 180].score.mean()
data[data.runtime >= 180].score.mean()
# What's the deal with the streations in the plot?

# The mean score for movies over 3 hours long is greater than that for movies 
# less than 3 hours long, but these values are skewed as the longer movies
# have few votes.

plt.scatter(data.runtime, data.votes, lw=0, alpha = .08)
plt.xlabel('Runtime (minutes)')
plt.ylabel('Votes')

data.votes.describe() # There are two War and Peace titles!
data[(data.title == 'War and Peace') & (data.year == 1967)].votes
data[data.title == 'Satantango'].votes
# Almost 75% of the movies are shorter than the above two.


plt.hist(data.votes, bins=200, color='#cccccc')
plt.xlabel("Votes") # Woah, that's not a normal distribution.  