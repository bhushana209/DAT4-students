David,

A very interesting and thorough analysis. You clearly understand the subject matter very well.

#Code:

* I know next to nothing about SQL, so I can be of little help other than to say that aspect looks pretty good to me.

* One totally minor, nitpicky stylistic issue: the Python style for [naming classes](https://www.python.org/dev/peps/pep-0008/#class-names) is to use the CapWords convention, e.g. `YearCalls` instead of `year_calls`.

* In terms of the substance of the code itself, I think there are some opportunties to increase the modularity of your classes and functions. As far as I can tell, the call_YYYY and call_tracts_YYYY classes all do the same thing, just for the different years.

	When calling a function from years_of_milwaukee.py, for example, it would be useful to be able to pass the year in question as a variable 		
			<pre><code>def __init__(self, year): 
		self.year = year</code></pre> 
	that tells the program which SQL database to pull up and then perform and return the data extraction and analysis you've defined. 
	There maybe be other opportunties in the controller, for example, assembling the different lists of low/med/high/upper approvals, accounts, originations, etc.

#Analysis:

* I wonder if there's a way in matplotlib to relocate the legend for the graph. Several times the graph is obscuring apparently important parts of the visualizations.

* Looking at the graphs you've generated, there seem to be some interesting trends. 

	* The [number of minority applications](https://github.com/Kibrael/DAT4-students/blob/master/david/CourseProject/minority%20applicaiton%20count%20tract.png) in low minority tracts is much higher than in other tracts, as are the [minority origination counts](https://github.com/Kibrael/DAT4-students/blob/master/david/CourseProject/minority_origination_counts.png). 

	* The [minority approval rate](https://github.com/Kibrael/DAT4-students/blob/master/david/CourseProject/minority%20approval%20rates.png) is also quite high in low minority tracts, while the division with the other tract levels is less clear cut.

* The trends I mentioned above suggest a couple of possible interpretations to me: that low-minority tracts are generally wealthier and therefore the minority applicants who do live in them are also wealthier/more creditworthy, OR that race/ethinicity is more influential in who is approved, that is, applicants from majority white tracts are favored regardless of income.

	These trends make me wonder about the role income/socio-economic status plays in your analysis. That is, should you control for the `ffiec_median_family_income` and/or `tract_to_msa_md_income` described in the data dictionary? 

	Put another way: in order to answer the question "Did the financial crisis disproportionately affect minority borrowers," must you compare the applications, originations, and approvals for poor neighborhoods that are low minority to poor neighborhoods that are mid, upper, and high minority, middle-income neighborhoods to middle-income neighborhoods, etc.? Perhaps ethnicity is statistically irrelevant for a wealthy applicant in a wealthy neighborhood but very relevant for a lower income applicant in a less affluent neighborhood.

I hope you find this helpful, any questions just let me know. Best of luck with your project.

