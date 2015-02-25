# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 20:35:35 2015

@author: deronhogans
"""

import pandas as pd
import numpy as np
trips = pd.DataFrame.from_csv('2PointB_January_Trips.csv', sep= ",", header=0, index_col=0)

trips['Status'] = trips.Status.map({'Meter Off': 1, 'Unable to Auth': 0, 'Cancelled':-1})

trips.Trip_Adjusted = trips.Trip_Adjusted.map({'Yes': 1, 'No': 0})

trips.Existing_Passenger = trips.Existing_Passenger.map({'Yes': 1, 'No': 0})

trips.dropna() 

trips.plot(kind='scatter', x='Discount_Applied', y='Existing_Passenger', alpha=0.3)

trips.plot(kind='scatter', x='Gross_Amount', y='Existing_Passenger', alpha=0.3)

trips.plot(kind='scatter', x='Trip_Adjusted', y='Existing_Passenger', alpha=0.3)

colors = np.where(trips.Fleet=='Cab', 'r', 'b')
trips.plot(x='Fleet', y='Existing_Passenger', kind='scatter', c=colors)