Hi Gary,

- The presentation is looking great! Good storytelling, and visuals to back up each point. That's exactly what we want a final presentation to look and feel like.

- Nice work extracting the question and answer data from your CSV! I like that you're concatenating all of the answers (for a given question) into a single variable.

- It's not yet clear to me that there is value in keeping the question and answer data separate, if the goal is unsupervised learning. In other words, it might be better to combine the question and answer data for each row. That way, you have more data to "learn" from for each observation.

- Regarding your clustering strategy, lines 78 to 88 is a good start. You've fit 3 clusters to your vectorized answers data, and you've printed out the labels for each "document" (meaning each row of data). What should you do from here?
    - Well, you would probably want to search for an optimal value of k (the number of clusters).
    - Then, you would want to (manually) look through a sample of documents from each cluster, to see if the clusters make sense!
    - If you're getting "meaningful" clusters, you could hand-label them at this point. If you're getting useless clusters, you will probably want to try a different value of k.

- For line 91, there's actually no value in running this line of code. You already "fit" your model to the answers data, and the purpose of "predict" is to predict a cluster for your out-of-sample data. But, you don't have any out-of-sample data at this point, so you're just fitting and predicting on the same data, and it will just generate the same cluster labels that you printed out in line 88.

- For line 92, there are a couple important points:
    - Keep in mind the different between the "fit" and the "transform" for the vectorizer. Fit learns the vocabulary (the features). Transform creates the matrix based upon that vocabulary. You fit and transform based upon answers, so if you're going to predict based upon questions, you should only run the transform method, not the fit method. Otherwise it will fail because the features will be different. It's complicated, I know :)
    - It looks like the transform step is having problems because there is some sort of invalid data in your questions data. If you run `questions.isnull().sum()`, you'll see that there are 2 nulls. I would get rid of those documents entirely.
    - As mentioned above, I'd probably recommend combining your question and answer data together. In that case, you never actually need to run a predict method for kmeans, just a fit method, in which case you can just get rid of this line of code entirely :)

- On line 86, you mentioned interpreting the TFIDF scores. You certainly could look at those scores and try to figure out the most interesting words from each document, but it's not yet clear to me whether doing those calculations would provide you with an actionable information. It could possibly come in handy if clustering is getting too distracted by uninteresting words (like it is clustering documents based on whether they contain the word "the" or not), but for the moment, I wouldn't focus on interpreting those scores.

- You mentioned on line 110 that you're not able to import lda. I would recommend trying to install it via `pip install lda` at the command line.

Nice job so far!
