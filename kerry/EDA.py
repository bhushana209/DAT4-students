# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 06:13:04 2015

@author: joneskm1


1) What data have you gathered, and how did you gather it?

I pulled NBA seasonal stats for every player from 1953 - 2015.
The file contains the following variables: name, age, team, games started, played, field goal, 2pt- field goals, 3pt field goals, effective shooting, free throw, rebounds, turnovers, blocks, steals, assist and pts
NBA Data pulled from GitHub user.


2)What steps have you taken to explore the data?
First looked at the head, shape,type and values to assess structure and missing values.
I realize there were alot of values missing due to change in data collected over time. 

Noticed many values missing(most because some werent considerd important until mid 70s. So instead of making those
#values zero, used the median(could use mean ). Post-1978, if player did not have value for specific variable then received a 0.

3) Which areas of the data have you cleaned?
Different attributes
Some players were categorize as just Guard or Forward, so made assumption and just replaced values to SG or SF

4)which areas still need cleaning?
 Where I just used the mean or median of a specific stat, I would like to find their positional average instead by all players. 
 
5) What insights have you gained from your exploration?
Most data has a positive skew
Want to do a scatterplot matrix to find correlation but seemed too cluttered. How do I just do a pearson correaltion?

6)Will you be able to answer your question with this data, or do you need to gather more data (or adjust your question)?
Yes, since I am trying to predict which players made the all nba team for their given season, i need to scrape that data from the basketball-reference website
and then and categorical variables to each player. Not sure how that dataframe would look though....will need to discuss further....

Also would be interested in pulling advane metric data to see if that could help produce a better model.


7) How might you use modeling to answer your question?
This is a classification question. Running this data in the K-NN model to predict position was promising, so that could be another way to predict whether they do or not.
I wonder if K-means would work....? OR perhaps recommendation systems could recommend which players make the 2015 teams based on past years performaners.....



"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

col_u = ["player","pos","age","bref_team_id","g","gs","mp","fg","fga","fg_","x3p","x3pa","x3p_","x2p","x2pa","x2p_","efg_","ft","fta","ft_","orb","drb","trb","ast","stl","blk","tov","pf","pts","season","season_end","scrape_time","data_source"]
players= pd.read_table("https://raw.githubusercontent.com/kjones8812/JonesGeneralAssembly/master/player_totals_1953_2015.csv",header = 1, sep = ',',names = col_u)

#Explore the dataframe
type(players)

players.head(10)
players.tail(10)

players.index
#players.columns
players.dtypes #mixture of data types(integers, floats,string objects )
players.shape # There are currently 18801 rows and 33 columns
players.values #dataframe as array
players.info() # Noticed many values missing(most because some werent considerd important until mid 70s. So instead of making those
#values zero, used the median(could use mean )


# post-1978, if player did not have value for specific variable then received a 0.

players[players.orb.isnull()]
players.orb.median()
players.orb.fillna(value=players.orb.median(), inplace=True) # modifies variable in place
players.orb.median()

# can i get the average by position using groupby?

players[players.drb.isnull()]
players.drb.median()
players.drb.fillna(value=players.drb.median(), inplace=True) # modifies variable in place
players.drb.median()

players[players.tov.isnull()]
players.tov.median()
players.tov.fillna(value=players.tov.median(), inplace=True) # modifies variable in place
players.tov.median()

players[players.blk.isnull()]
players.blk.median()
players.blk.fillna(value=players.blk.median(), inplace=True) #
players.blk.median()

players[players.stl.isnull()]
players.stl.median()
players.stl.fillna(value=players.stl.median(), inplace=True) #

players.info() # Check 
"""
For Field Goals(2p,3p, fg) Have to assess slightlty differently.
"""

test = players[players.fg_.isnull()]
#Find who out who didnt take fgs
#also missing efg, 2p, 3p..through out all years...safe to assume these guys didnt get much PT.
#use conditonal filtering...where both conditions are true in

test = players[players.fg_.isnull()].fillna(value = 0)

players.fillna(value = test, inplace =True)
players.info()

#players[players.season_end <= 1978].x3p_.fillna(value =players.x3p_.mean(), inplace = True)
#players[(players.season_end > 1978) & (players.season_end != 2015)].fillna(value = 0, inplace = True )
#these line did not work.....


players['x3p'].isnull().sum()# But 3ps made and attempted both have 4291 missing values.
players['x3pa'].isnull().sum()
players['x3p'].isnull()[players.season_end <= 1978]
players['x3pa'].isnull()[players.season_end <= 1978]

players.x3p.median()
test = players[players.season_end <= 1978].x3p.fillna(value = players.x3p.median())
players.x3p.fillna(value = test.astype(int), inplace =True)
players.x3p.median()

players.x3pa.median()
test = players[players.season_end <= 1978].x3pa.fillna(value = players.x3pa.median())
players.x3pa.fillna(value = test.astype(int), inplace =True)
players.x3pa.median()

players.x3p_.median()
test = players[players.season_end <= 1978].x3p_.fillna(value = players.x3p_.median())
players.x3p_.fillna(value = test.astype(float), inplace =True)
players.x3p_.median() 

players.info() # Check

players['x3p_'].isnull().sum()
players[players.x3p_.isnull()]
test2 = players[players.season_end > 1978].x3p_.fillna(value = 0)
players.x3p_.fillna(value = test2, inplace = True)
players['x3p_'].isnull().sum()

players['x2p_'].isnull().sum()
players[players.x2p_.isnull()]
test2 = players.x2p_.fillna(value = 0)
players.x2p_.fillna(value = test2, inplace = True)
players['x2p_'].isnull().sum()

players.info()
players['ft_'].isnull().sum()
players[players.ft_.isnull()]
test2 = players.ft_.fillna(value = 0)
players.ft_.fillna(value = test2, inplace = True)
players['ft_'].isnull().sum()

players.info() # Check


players.describe()
# in some columns, count is 18802, and in others its less. There are some missing values.
players.isnull().sum() # No missing values

#delete string variables
del players['season']
#maybe should convert two variables(season_start, season_end)
del players['scrape_time']
del players['data_source']


#all counts in variables are now equal
players.shape # 18801 rows, 30 columns

players.pos.value_counts() #find values by position
#Several players positions have been described as just G or F. Who are they?
players[players.pos == 'G']
players[players.pos == 'F']

#based on prior exisiting assumptions, I changed replaced all values of guards as Shooting guards and Forwards as Small Forwards
players2 =players.replace('G','SG')
players3 =players2.replace('F','SF')
players3.pos.value_counts()


#Descriptive Statistics

players3.groupby('pos').pts.describe()
players3.groupby('pos').ast.describe()
players3.groupby('pos').tov.describe()
players3.groupby('pos').stl.describe()
players3.groupby('pos').blk.describe()
players3.groupby('pos').trb.describe()
players3.groupby('pos').mp.describe()


# Bar plot: Shows the frequency of possible values for a categorical variable
# lets look at the number of players by position
players3.pos.value_counts().plot(kind='bar', title='Players per Position')
plt.xlabel('Position')
plt.ylabel('Count')
plt.show() # show plot window (if it doesn't automatically appear)
plt.savefig('Players by Position.png') # save plot to file



players3.pts.hist( by=players3.pos, bins = 10)
players3.ast.hist( by=players3.pos, bins = 10)
players3.tov.hist( by=players3.pos, bins = 10)
players3.stl.hist( by=players3.pos, bins = 10)
players3.blk.hist( by=players3.pos, bins = 10)
players3.trb.hist( by=players3.pos, bins = 10)
players3.mp.hist( by=players3.pos, bins = 10)


# Most variable except minutes played distributions are skewed to the right.
#postive skew suggests the mean is to the right of the peak value

#Whats the best way to run a scatter plot matrix or do I want to just find pearsons correlation between all the variables ?


def ranker(df):
"""Assigns a rank to each employee in any given season based on pts, with 1 being the highest points in a season.
Assumes the data is DESC sorted."""
df['pos_rank'] = np.arange(len(df)) + 1
return df

#how do I find the best ranked skilled positions for each year instead for any given season? for loop?

players3.sort('pts',ascending = False, inplace = True)
players3 = players4.groupby('pos').apply(ranker)
rankBy_pts = players3[players3.pos_rank == 1]

players3.sort('ast',ascending = False, inplace = True)
players3 = players3.groupby('pos').apply(ranker)
rankBy_ast = players3[players3.pos_rank == 1]

players3.sort('stl',ascending = False, inplace = True)
players3 = players3.groupby('pos').apply(ranker)
rankBy_stl = players3[players3.pos_rank == 1]

players3.sort('tov',ascending = False, inplace = True)
players3 = players3.groupby('pos').apply(ranker)
rankBy_tov = players3[players3.pos_rank == 1]

players3.sort('blk',ascending = False, inplace = True)
players3 = players3.groupby('pos').apply(ranker)
rankBy_blk = players3[players3.pos_rank == 1]

players3.sort('trb',ascending = False, inplace = True)
players3 = players3.groupby('pos').apply(ranker)
rankBy_trb = players4[players4.pos_rank == 1]

players3.sort('mp',ascending = False, inplace = True)
players3 = players3.groupby('pos').apply(ranker)
rankBy_mp = players4[players3.pos_rank == 1]


#NEED ALL-TEAM NBA DATA(need to find the what distribution of players have been on all nba team)
# Find metric that bests explains players individual performance(use that as a ranking metric) does that match up with who was voted on all nba team?

