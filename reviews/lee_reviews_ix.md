## Peer Review
### Alex Lee for Frank Ix

#### Strengths

This is an interesting problem, and I think that the clustering approach outlined here is a good one given the nature of the question being asked.  I also think K-means is a good place to start with it, as it is pretty straightforward, and the initial choice of variables to look at (distance, speed) are logical ones to begin with.

#### Comments on areas for potential improvement

I see that you're calculating average MPH and using that as a variable to cluster on, which I think is a good idea (generating new features from data) -- however, it's based on data that you have also calculated from the same trips (max speed, and presumably min speed also?), which I think might be good to keep in the clustering algo as well.  You could include both the more "straightforward" calculated features (distance, min speed, max speed) per trip, as well as the "derivative" features (like average speed), and throw all those dimensions into the clustering algo at once.

#### Questions

- Is there a particular reason to normalize the variables in this case?  Also, if they are being normalized anyway, is there a need to convert specifically to MPH in your main loop, or could you just leave it as meters/sec?
- The initial plot of distance vs. speed appears to be more of a curvilinear spread of data -- as such, are there more dimensions that you can add to the data to make it something more "clusterable", or alternatively different transforms in addition to z-scores that might give K-means something more to work with?

#### Comments on code

- In your main loop, the nested for loop appears to be grabbing the wrong start and end points, though I am not certain of this.  When I tried "manually" stepping through it by running some individual code snippets, it appeared to be defining "start" as the final row in drive, and end as the first row (so off by one from what you actually want, and wrapping backwards through the data).  This might explain some of the weird speed values you're seeing, but it also may just be the case that my attempts to manually create what the loop is doing aren't accurate.

#### Suggestions for next steps

I would probably take a look at generating some additional features from the data to give a clustering algo a bit more to work with.  I think that where you have started is a good place, but from the inital plots that you've done, it looks like you're primarily just seeing a (reasonable) linear relationship of increasing average speed with increasing trip length.  Trying to find some more dimensions that you can derive from the data they've provided could potentially help define some clearer clusters that identify the kinds of outliers you're looking for (and you've identified a few of these yourself already in the Project Explanation).  Overall looks like you're on a good track to me.
