Akshay,

This is an interesting project. I just have a few remarks on the code and then a few ideas about analysis.

#Code:

* Typo on line 67, `(gtd.iyear>1980)`: I think you want 1990 given the plot you create below that is 'U.S. Terrorist Attacks by Target Type, 1990-2014.' 

* It might be a good idea to map the target type values from the GTD to the tickers for the indices you think are the most relevant, e.g. `{'airlines': '^XAL'}`. 
	
	It might even be a good idea to write a separate function to map the target type value and country to specific country indices:
	airlines + US = DJUSAR, airlines + UK = FTSE100, etc., if you intend to get that country-specific.

	You could then rewrite your `stockdata` function to automatically retrieve the ticker data based on the target of the particular event, the event's location, and the time frame you specify. 

* I'm a little lost in your `stockdata` function. You list the `industry` and `unit_of_time` as input variables, but you don't seem to use those inputs anywhere in the body of the function other than in `unique_dataframe_name`. Perhaps you want to filter the attacks by industry and then set the timedelta to the unit of time? Something like

	<pre><code>for attack in df.iterrows():
		if df['industry'].iloc[attack] = industry:
			start_time = ...
			end_time = start_time + datetime.timedelta(unit_of_time = timedelta)
			...</code></pre>

	There's probably a better/correct way to do that, but that's what jumped into my head.

#Analysis:

* There are many interesting analytic possibilities. For example:

	* Are some industries more sensitive to terrorism than others?
	* Which industries are most financially affected by terrorism?
	* Is a particular type of attack more effective in terms of impacting valuations than other types?
	* Which industries are most resilient to terrorism, that is, which industries' values return to normal the quickest after an attack?
	* Given an attack on industry x, can you predict the impact on industry x's valuation in the days, weeks, and months ahead?
	* Given an attack of type x on industry y, can you predict the impact on industry y's valuation in the days, weeks, and months ahead?

I hope this is useful. If you have any questions please let me know. Best of luck on your project.
