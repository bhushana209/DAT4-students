## MetroMetric
*Austin's final project*

* This project will develop one or more metrics for performance of WMATA's next bus algorithm
* The primary data source will be the public API, which can provide bus locations and predicted arrival times
  * Documentation here: http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf
  * My data strategy is:
    1. Set up a script to capture data on bus position and expected arrival times for routes of interest at regular intervals
    2. Visually inspect data and explore initial findings
    3. Develop an algorithm to assign buses unique identifiers so they can be evaluated
    4. Using these bus records, evaluate the timeliness of the bus (that is, if it was expected in 10 minutes, how often was it within a certain delta of that time)
* I am choosing this project because I am interested in transit and urban science

|Question|Possible method|
|--------|---------------|
|How good is DC’s next bus algorithm overall?| Develop a general definition of 'on time' and evaluate a sample of routes and stops
|How does this depend on route?| Facet the overall data set by route, using some local, some express, and other variety
|How does this depend on weather?| Capture data during a weather event (rain or snow) and compare to a similar day
|How does this depend on time of day?| Graph average timeliness by time of day, normalized by route and day of week
|How does this depend on day of week?| Graph average timeliness by day of week, normalized by route and time of day