Brennan, if i didnt know this was intended to 'predict market trends one day into the future, i would expect it to cure cancer (at least).  This is very ambitious and aggressive...i like t.

These are my observations section by section:
---------------------------------------------
- in your byline you state "Current status: Models are still close to a coin flip for predicting 1 day into the future, but results are more enouraging for predicting whether or not the S&P 500 will rise or fall 10-90 days out." but i do not know whether you are talking about generic/published/accepted models or the ones you will demonstrate in the forthcoming code.  this line perhaps needs a rewrite.

- in section [2] i assumed these items to be data stores of the corresponding market forces.  i went to Quandl.com and:
	- first searched on "FRED/GOLDPMGBD228NLBM" with no results. 
	- then i searched on "GOLDPMGBD228NLBM" with no results.  
	- then isearched on 'gold' with lots of results but nothing that looked like it was your data.
	- i gave up thinking maybe document what those variable declaration are with a lengthier comment

- in section [26] dataframe output is very clean and easy to understand...running describe() is good for me personally to understand the scope/breadth of the data with which i am working.
-  in section [30-36] you use a standard LOG/REG train/test model to make predictions plot a ROC curve which i could run/see if i could get Quandl imported. : ))
- in section [37] you run a coin flip to demostrate the proximity of the two modeling techniques.
- in section [39] you iterate on train_test_split_logreg_plot to see...? * im not sure here *
- in sections [50 to 76] you continue to add features to try to get an ever closer fit to the * ? *
- in section [78-9] you plot all modeled data to get a visual of cumulative models run.
- i dont know anything about Bollinger values 
- lots of great use of differnt forms of machine learning, models, iterating against the data, trial and error and balls.

> Written with [StackEdit](https://stackedit.io/).