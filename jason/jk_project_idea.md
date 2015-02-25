# Project Proposal: Predicting Startup Funding Based on Patent Grants

I would like to explore if one can predict how much funding a startup will receive based on the content of the patents the company has been granted.

Founders of startups are generally motivated to create a new product or service and to make money doing so. A key component of this process is creating (and protecting) intellectual property, often in the form of filing for patents. 

The big money that invests in startup companies, angel investors and venture capital firms, must gauge whether or not to fund different efforts based on factors such as the size of the market, the personality types of the founders, and, of course, the quality of the product or service itself. 

The data sources I plan to use are:
* The [USPTO Patent Grant Full Text repository](https://www.google.com/googlebooks/uspto-patents-grants-text.html) hosted by Google
	* Contains txt and/or xml files for all patents granted since 1976.
	* Appears that the records are fairly complete.
* The [Startups and Venture Capital collection](https://www.quandl.com/c/usa/usa-startups-venture-capital) on Quandl. 
	* I haven't explored this collection in depth yet, so I can't say how complete the records are.
	* I'm hoping this is granular enough for my purposes. If not, there are other options, such as [CB Insights Venture Capital Database](https://www.cbinsights.com/venture-capital-database), but those require payment.