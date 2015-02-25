## Driver Telemetric Data (kaggle)
Frank Ix
Exploration and Analysis Plan

*Gathering*

I have downloaded the kaggle data zip, which contains data for 3000+ drivers, each with 200+ driving trips. Each trip contains x and y coordinates that map driving location over time.

I plan to compile all 200 trips for each driver into one single data set, either consisting of a dictionary of lists:

driver 1 = {
	"drive_1": [
		{'x':0, 'y':0, 'x':0, 'y':0,...}
	]
}

or figure out a way to reduce the x/y's into a single vector number? Not sure if possible, but it would allow me to create a table with each row set to one trip. 

*Analysis*

I plan to do a couple of basic things before building a model/algorithm. 

First, I have begun to think through the types of information I can gather from the x/y data that will allow me to build a driver profile, including:

1. Driving speed
2. Driving distance
3. Frequency of turns
4. Repeating course (i.e. turning around/getting lost)
5. Repeating trips

Second, I plan to do basic scatterplotting of these metrics for select drivers to see if obvious outliers exist to hopefully hone my modeling approach.

As for my model, my initial thought is that cluster analysis (maybe this one? [GMM](http://scikit-learn.org/stable/modules/mixture.html#gmm-classifier)) makes the most sense as it will allow me to group results and make probability assignments about whether a drive was driven by that assigned driver or not (a requirement in the competition).

I would also like to explore the idea of using map-reduce/hadoop to run the model across all drivers, if that makes sense. Would be cool to learn how to do that, even if its a bit of overkill.
