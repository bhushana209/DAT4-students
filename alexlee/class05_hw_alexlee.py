"""
Class 05 Homework: pandas Data Wrangling and Exploration
Alex Lee
1/9/2015
"""

#%matplotlib inline #ipython magic command
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# set up column names and read the file FROM URL; changed read_csv to read_table for txt data
names = ['imdbID', 'title', 'year', 'score', 'votes', 'runtime', 'genres']
data = pd.read_table('http://bit.ly/cs109_imdb', delimiter='\t', names=names).dropna()
print "Number of rows: %i" % data.shape[0]
data.head()  # print the first 5 rows

# skipped pasting in example code of how string.split() method works

clean_runtime = [float(r.split(' ')[0]) for r in data.runtime]
data['runtime'] = clean_runtime
data.head()

#determine the unique genres
genres = set()
for m in data.genres:
    genres.update(g for g in m.split('|')) #update method unions the calling set with passed objects
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

#sum sums over rows by default
genre_count = np.sort(data[genres].sum())[::-1]
#updated the below code to make it actually name the indices
pd.DataFrame({'Genre Count': genre_count}, index=data.columns[7:len(data.columns)])

#axis=1 sums over columns instead
genre_count = data[genres].sum(axis=1)
print "Average movie has %0.2f genres" % genre_count.mean()
genre_count.describe()

#movies by decade
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

# skipping the sections regarding manual construction of small multiples

"""
Additional analysis for homework
================================

Plots can be found in the GitHub repo along with this file, if you don't want to reproduce them yourself with the code below.

Interesting fact #1:

Lowest-average movie scores have been trending downwards over time.  This could possibly be due to selection bias in terms of what ends up on IMDB, and/or just a greater volume of movies produced leading to more opportunities for terrible movies.

"""
# code for interesting fact #1:
plt.plot(data.groupby(data.year).score.min().index, data.groupby(data.year).score.min())
plt.xlabel('Year')
plt.ylabel('Minimum IMDB Score for Year')
plt.title('Lowest IMDB Scores by Release Year')
plt.savefig('lowest_scores_by_year.png')

"""
Interesting fact #2:

Movie runtime is a more widely-dispersed variable for higher scoring movies, almost monotonically so (judging by the scatterplot shape).  This could be reflective of "more opportunity for better content" in longer movies, or the impact of a hidden variable such as budget which, at low levels, might be strongly correlated with short runtime for low-rated movies, but not correlated as much when it increases to higher levels.  It could also just be a spurious correlation that produces an interesting pattern.

"""
# code for interesting fact #2:
plt.scatter(data.runtime, data.score, alpha=0.2)
plt.xlabel('Runtime (minutes)')
plt.ylabel('IMDB Score')
plt.title('IMDB Scores by Movie Runtime')
plt.savefig('scores_by_runtime.png')

"""
Bonus intersting fact / plot:

Both the order in which the data are presented in the table as it is downloaded, and also the order of the IMDB IDs, are correlated with scores in such a way that cumulative average score is (almost) monotonically decreasing for both.  When plotting against a random ordering (shown in green in the plot), the as-is sequence (blue) and IMDB ordered ID sequence (red) are very obviously patterned.

In and of itself this doesn't tell you much, but depending on a learning application, it is a strong reminder that it is almost always a good idea to randomize the order of your data, lest the order itself become a hidden variable that the algorithm inadvertently "learns" from.

"""
# code for bonus interesting fact

data2 = data.sort(columns = 'imdbID')
data2['id_seq'] = np.arange(9999) #fake reindex
data2['cum_avg_score'] = data2.score.cumsum()/(data2.id_seq + 1)
data3 = data2.sort()
data2['cum_avg_score_asis'] = data3.score.cumsum()/(data3.index+1)
plt.scatter(data2.id_seq, data2.cum_avg_score, color='r', alpha = 0.2, label='By IMDB ID')
plt.scatter(data2.index, data2.cum_avg_score_asis, color='b', alpha=0.2, label='As-Is')
np.random.seed(12345)
randomized = np.random.permutation(len(data))
data2['random_seq'] = randomized
data4 = data2.sort(columns='random_seq')
data4 = data4.reindex(np.arange(9999))
data2['cum_avg_score_random'] = data4.score.cumsum()/(data4.index+1)
plt.scatter(data2.random_seq, data2.cum_avg_score_random, color='g', alpha=0.05, label='Random order')
#interesting... order of these data, and of the IMDB IDs, is highly correlated with score for some reason
plt.xlabel('Sequence #')
plt.ylabel('Cumulative average score')
plt.title('Cumulative average score for alternative sequences')
plt.legend(loc='best')
plt.savefig('cum_avg_scores_by_seq.png')
