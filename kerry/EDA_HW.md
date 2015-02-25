Kerry Jones
DAT4

Please look at EDA.py for further information.


1) What data have you gathered, and how did you gather it?

I pulled NBA seasonal stats for every player from 1953 - 2015.
The file contains the following variables: name, age, team, games started, played, field goal, 2pt- field goals, 3pt field goals, effective shooting, free throw, rebounds, turnovers, blocks, steals, assist and pts.
NBA Data pulled from GitHub user.


2)What steps have you taken to explore the data?
First looked at the head, shape,type and values to assess structure and missing values.
I realize there were a lot of values missing due to change in data collected over time. 

Noticed many values missing(most because some weren’t considerd important until mid 70s. So instead of making those
#values zero, used the median(could use mean ). Post-1978, if player did not have value for specific variable then received a 0.

After I cleaned, looked a basic descriptive statistics and plotted some bar charts and histograms. 

3) Which areas of the data have you cleaned?
Different attributes
Some players were categorize as just Guard or Forward, so made assumption and just replaced values to SG or SF

4)which areas still need cleaning?
 Where I just used the mean or median of a specific stat, I would like to find their positional average instead by all players. 
 
5) What insights have you gained from your exploration?
Most data has a positive skew
Want to do a scatterplot matrix to find correlation but seemed too cluttered. How do I just do a pearson correlation?

6)Will you be able to answer your question with this data, or do you need to gather more data (or adjust your question)?
Yes, since I am trying to predict which players made the all nba team for their given season, i need to scrape that data from the basketball-reference website
and then and categorical variables to each player. Not sure how that dataframe would look though....will need to discuss further....

Also would be interested in pulling advance metric data to see if that could help produce a better model.


7) How might you use modeling to answer your question?
This is a classification question. Running this data in the K-NN model to predict position was promising, so that could be another way to predict whether they do or not.
I wonder if K-means would work....? OR perhaps recommendation systems could recommend which players make the 2015 teams based on past years performaners.....


