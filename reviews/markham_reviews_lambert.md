Nice work so far, Jen. The PDF has a good summary of your goals, your approach, and what you've learned so far by exploring the data.

Here are some comments:

- The Python script (FacebookData.Jlambert.py) in your zip file is empty... do you have a script I can look at?

- In your final project, it would be great to see some real-life Facebook posts from your dataset, along with the associated data. This would help to give the reader more context about the type of posts DoS creates, and a snapshot of some key data points about those example posts.

- It would also be great to see some visualization of your data... maybe histograms or scatterplots for a few of your features? Maybe separated out by region? The data you have is so interesting, and people can all relate to Facebook, so it would be great to show off some of this data visually.

- Regarding the creation of dummy variables, you can see some example code in [this notebook](http://nbviewer.ipython.org/github/justmarkham/DAT4/blob/master/notebooks/08_linear_regression.ipynb) on linear regression, and some better example code in the bottom part of [this notebook](http://nbviewer.ipython.org/github/justmarkham/DAT4/blob/master/notebooks/15_decision_trees.ipynb) which we will be talking about in class tomorrow!

- Regarding the extraction of text-based features, the simplest way would be to create a document-term matrix like we did in the Naive Bayes class, and then use those counts as additional features. That might be a good starting point, and then we can figure out how to improve on that approach.

- It sounds like "shares per user reached" will be your response variable, is that correct? If so, you'll want to use a regression method (such as linear regression) rather than a classification method (such as logistic regression).

- Regarding Random Forests, we will be talking about that in class tomorrow!
