## Data Exploration and Analysis Plan

**What data have you gathered, and how did you gather it? 
We actually had to gather data from two Facebook pages in each of the six regions (how the State Department divides the world) for a project at work, so I decided to merge this with my GA project a bit - but look at a different question. For my GA project, I want to try to predict the number of Facebook shares a piece of content will receive based on the various attributes available in Facebook Insights data.  I downloaded the data from each Facebook Insights and merged them in one large data set. I also made a call using SQL from a database we had at work to export all the theme tags for ShareAmerica URLs in the Facebook posts and imported this data as one column in my data set.

**What steps have you taken to explore the data? 
In excel (data was downloaded in a .csv file), I've looked at the number of Facebook posts, the proportion of ShareAmerican content for each Facebook page, and the average share rates for each page.

**Which areas of the data have you cleaned, and which areas still need cleaning? 
I did add a column for thematic tags - but now I will have to add tags to all non-ShareAmerica content in a consistent fashion as the tags that have been added to the Facebook posts that included ShareAmerica content. I imagine I will also have to extract the tags from the column and break them into separate columns and turn them into dummy variables. Right now, all the tags for ShareAmerica content are dumped into one column - but there could be as many as 3-4 tags in the one cell.

**What insights have you gained from your exploration? 
Pages use ShareAmerica content at pretty different rates - also the average shares per post vary pretty greatly between different pages. Some pages post 7-8 times a day; other pages post 1-2 times a day.

**Will you be able to answer your question with this data, or do you need to gather more data (or adjust your question)? Yes!

**How might you use modeling to answer your question? Since I have a continuous prediction variable (number of Facebook shares), I may use a linear regression.