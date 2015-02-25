## **Alternative Question Ideas/Topics:**

 **MyBrother’s Keeper Initiative:** 
A few months back President Obama started a government initiative to use statistical data to understand the critical indicators effect 
the life outcomes for minority boys and young men. I am interested in looking at indicators across an array of 
domains: health, nutrution, poverty, education, economic opportunity, crime, to see how valuable they are at predicting
whether a minority ends up in college or in prison. The main issue with this idea is the availability of data at a local scale. 
It might be interesting to see whether there’s enough openDC data avaliable to try and predict these type of outcomes in dc. 

[My Brother's Keeper Initiative] (http://mbk.ed.gov/data/)

**Sentiment analysis of product reviews from amazon.**

[Amazon Product Data](http://snap.stanford.edu/data/web-Amazon.html)

## Kaggle Competitions:

**1) Using Telematic Data to identify a driver signature**
Automobile insurers are interested in using telematics data to measure the quantity and quality of driver’s behavior 
to make better pricing decisions. The goal of competition is to develop an algorithmic signature of driving type. 
Does the driver take long trips? Short? highway trips? back roads? Do they accurate hard from stops? 
Do they take turns at high speeds? 

**Data:** There are over 200 .csv files. Each representing a driving trip. The trips are recordings of the car's 
position (in meters) every second and look like the following:
x,y
0.0,0.0
18.6,-11.1
36.1,-21.9

[Telematics Competition] (http://www.kaggle.com/c/axa-driver-telematics-analysis/data)


**2) Predicting Forestry Coverage**
Using cartographic variables to classify forest categories. The study area consists of 565892 observations. 
The goal is to try and predict whether they fall in one of seven catgorical types:

1 - Spruce/Fir

2 - Lodgepole Pine

3 - Ponderosa Pine

4 - Cottonwood/Willow

5 - Aspen

6 - Douglas-fir

7 - Krummholz

There are 13 distinct variables. 

1. **Elevation** - Elevation in meters

1. **Aspect** - Aspect in degrees azimuth

1. **Slope** - Slope in degrees

1. **Horizontal_Distance_To_Hydrology** - Horz Dist to nearest surface water features

1. **Vertical_Distance_To_Hydrology** - Vert Dist to nearest surface water features

1. **Horizontal_Distance_To_Roadways **- Horz Dist to nearest roadway

1. **Hillshade_9am (0 to 255 index)** - Hillshade index at 9am, summer solstice

1. **Hillshade_Noon (0 to 255 index) **- Hillshade index at noon, summer solstice

1. **Hillshade_3pm (0 to 255 index)** - Hillshade index at 3pm, summer solstice

1. **Horizontal_Distance_To_Fire_Points** - Horz Dist to nearest wildfire ignition points

1. **Wilderness_Area** (4 binary columns, 0 = absence or 1 = presence) - Wilderness area designation

1. **Soil_Type** (40 binary columns, 0 = absence or 1 = presence) - Soil Type designation

1. **Cover_Type** (7 types, integers 1 to 7) - Forest Cover Type designation

This particular interesting because this is typically done using imagery. 

[Forestry Competition](http://www.kaggle.com/c/forest-cover-type-prediction)

