# Predicting solar flare events using sunspot group data.


* Satellites used for telecommunications and navigation operate in the high energy low density plasma environment of geosynchronous Earth orbit (GEO).
* Powerful eruptions on the surface of the sun eject high energy charged particles that increase the density of this plasma and can lead to increased satellite surface charging or failure.
* One of the areas that I have done research in is the development of transparent conductive oxides for spacecraft surface charge mitigation.  This was purely a materials science problem, and the possibility of designing a proactive charge mitigation system was not within the scope of the research plan.
* It is known that solar flares are associated with sunspot activity.
* Several observatories (NOAA, NASA, USAF, NRL) closely monitor the sun, and have made flare/sunspot data accessible online.
* The application of machine learning to solar flare prediction is an active research topic that is still in its early stage.
* I have decided to build upon [previous work conducted at the University of Bradford](http://spaceweather.inf.brad.ac.uk/library/publications/solarphysic1.pdf) in which solar flare event data were correlated to sunspot group data.  
* They were able to predict a flare occurence within a time window of six hours, and proposed a hybrid neural net/support vector machine method to increase prediction accuracy.

* I have written a script that accesses the NOAA space weather ftp and writes two .csv files containing data on solar flare events and sunspot groups respectively.
* The data needs to be pared down so that only sunspot groups and flare events with matching NOAA numbers remain.
* The flare measurement and sunspot measurement need to occur relatively close to one another.  Previous work chose six hours.  I will first need to 
clean up the date codes and verify that the times are in UTC in both datasets.

