Hi Frank, thanks for including all the code and the data, that's helpful.

Here are a few thoughts:

- Regarding the wacky numbers for mph_maxlist, that's because there is a bug in your code when creating dst (and thus mph). I couldn't immediately identify the cause because I'm not familiar with iterrows, but you're creating an mph_list that looks like this: [0, 20, 35, 85, 135], when it should look like this: [0, 20, 15, 50, 50]. In other words, you're computing cumulative values instead of a new value for each pair of data points. Here's some code I wrote that iterates through `data` instead of `drive` and works properly:

```python
for i in range(len(data)-1):
    start = np.array([float(data[i][0]), float(data[i][1])])
    end = np.array([float(data[i+1][0]), float(data[i+1][1])])
    dst = dist.euclidean(start, end) / 1609.34
    dist_list.append(dst)
    mph = dst*60*60
    mph_list.append(mph)
```

- If you convert the data to floats as you read them in, rather than each time you are building a new feature, you will save yourself a lot of work in the end because it will simplify the rest of your code.

- Whether or not normalization is useful/necessary depends on the particular application. It's good that you are thinking about it!

- Clustering is certainly one way you could go about solving this problem. However, think about how you are ultimately going to scale this up and make predictions for all drivers, not just one driver. Are you going to cluster each driver individually? Presumably each driver will have a different number of clusters... is your code going to compute an ideal number of clusters for each driver? And then how will it calculate probability of belonging to the clusters? At least to me, it would seem very challenging to write clustering code that will generalize across all drivers yet be able to make useful predictions for each individual driver.

- If it were me, here's the kind of process I would use: For driver 1, I would compute their mean trip length across all trips. Then, for each of their trips, I would assign a probability that it was their trip by how close the given trip length is to their mean trip length. I would write a loop to do the same thing for all drivers, and then submit the predictions to see how I'm doing. It's an unsophisticated model, but you have to start somewhere! I can't stress enough how important it is to get a working end-to-end process for making predictions ASAP. Because you have unlabeled data, literally the only (simple) way to evaluate your model is to make predictions and see how you are doing on the public leaderboard. Until you start submitting predictions, you will have no idea as to whether any approach you use actually makes sense. But once you have that end-to-end process, you can add a new feature and see whether it helps or hurts your model!
