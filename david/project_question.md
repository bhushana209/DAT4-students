#Data Science Course Project Proposal
##Analysis of Home Mortgage Disclosure Act (HMDA) data over time in a set geography

* My data set will be multiple years of the Loan Application Register (LAR)
* These files can be found at either www.consumerfinance.gov/hmda or www.ffiec.gov/hmda
* *italic*The files are quite large (approximately 18 million rows) and are not practical to host on github

###About the data:
    Each row has over 20 data elements and represents one mortgage loan. HMDA data is commonly paired with Census tract or MSA level data prior to analysis. This is done to show mortgage disparities across demographic groups. 

###About my current work:
    I am currently working on a project to replicate the aggregate and disclosure reports served at www.ffiec.gov/hmda. These reports are manually error checked at great cost and our hope is to reduce the cost and/or increase the value of the reports. Ideas for improvement include visualizing the reports, building dashboards, and producing data-embedded graphics to be served at consumerfinance.gov.

###What question do I want to answer:
    One of the major issues that government served reports have is that they do not offer a time-based perspective in the data. I hope to do some exploratory analysis that reveals which HMDA variables show significant (and meaningful) change over time in a specific geography.
    *bold*Which data fields, when visualized through time, would community groups benefit greatly from?

###Value proposition:
    Developing a visualized dashboard requires an understanding of what information people need to answer their questions. As a federal agency, our group of stakeholders is quite varied. Uncovering which HMDA variables show the greatest change over time and which variables provide the most utility when plotted over time will allow the construction of a meaningful visualization too. The use of javascript and/or D3 will provide a non-proprietary visualization engine that does not restrict access based on software buy-in.

###Project proposal:
    I plan to spend an initial phase reading through community reports to determine which variables are high-utility to different groups. Taking these variables for a specific geography such as one metropolitan statistical area (MSA), I will plot them over several years to see what changes have occured. 

<<<<<<< HEAD
    I am currently interested in seeing if there is a correlation in the value of home loans to racial category. Plotting the change in home loan value by race over time and comparing to the change in average home price may give some interesting information on home purchase preference/power by racial groups. Relied upon income is available in the HMDA data set to use as a control during this analysis.
=======
    I am currently interested in seeing if there is a correlation in the value of home loans to racial category. Plotting the change in home loan value by race over time and comparing to the change in average home price may give some interesting information on home purchase preference/power by racial groups. Relied upon income is available in the HMDA data set to use as a control during this analysis.
>>>>>>> 1ed5a7298803ec82a748d1c74bd857016595bb22
