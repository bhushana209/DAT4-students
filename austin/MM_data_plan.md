## Metro Metric Data Plan

* I need to generate the data set for the project from WMATA APIs
* I have explored the WMATA APIs for what data is available and determined that with 3 available APIs I can collect the needed data for the project
* I wrote a test script to access each API and scoped the fields required
* Initial estimates of data collection needs may exceed API allowance (50,000 calls per day and 10 calls per second. In promising discussions to aquire a temporary key with higher limits
* Result of the data pull will be a data frame of prediction events. 
* Specific data fields and the releavant API are below. NBP = next bus prediction. BP = bus position. RD = Route Data

| Element | API | Notes |
|---------|-----|-------|
|PID|N/A|Assigned as internal identified
|Route|NBP|name of the route
|Direction|BP|direction of travel
|StopID|NBP|stop identified, used to join record with stop location
|StopLat|RD|stop latitude
|StopLon|RD|stop longitude
|BusID|NBP|idetified of the bus
|TripID|NBP|idenifies the trip
|BusLat|BP|bus latitude
|BusLon|BP|bus longitude
|Date|N/A| date of prediction
|TOD|N/A| time of day of prediction
|Temp|N/A| temperature
|Weather|N/A| weather event?
|PA|NBP| predicted arrival time in minutess
|AA1|NBP| when the bus arrived by NBP prediction (method 1)
|AA2|BP| when the bus arrived by bus position
