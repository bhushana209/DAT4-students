# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 09:12:34 2015

@author: craig.m.lennon
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Import goes sunspot data
sunspot = pd.read_csv('C:\Users\Craig\Documents\Python_DS\GA_DS\DAT4-students\craig\USAF_sunspot_1982_2014.csv', dtype = object)

clean_sunspot = sunspot[['data_code_date', 'UTC_obs', 'NOAA_USAF_spot_num', 'zurich', 'penumbra', 'compactness', 'number_of_spots', 'area']]

# only cases with complete sunspot class descriptions, ie zpc values

clean_sunspot = clean_sunspot[clean_sunspot.zurich.notnull()]
clean_sunspot = clean_sunspot[clean_sunspot.penumbra.notnull()]
clean_sunspot = clean_sunspot[clean_sunspot.compactness.notnull()]

# check NaN sum
# clean_sunspot.compactness.isnull().sum()

'''
The data_code_date entry needs to be edited
'''
# clean up the trailing decimal point and zero
clean_sunspot.data_code_date = [item.replace('.0', '')  for item in clean_sunspot.data_code_date] 






clean_sunspot['year'] = [int('19' + date[2:4]) if int(date[2:4]) >=81 and int(date[2:4]) <=99 else int('20' + date[2:4]) for date in clean_sunspot.data_code_date]
clean_sunspot['month'] =  [int(date[4:6]) for date in clean_sunspot.data_code_date]
clean_sunspot['day'] =  [int(date[6:8]) for date in clean_sunspot.data_code_date]



UTC_time = [time[:-2] for time in clean_sunspot.UTC_obs]

clean_UTC_time = []

for time in UTC_time:
    if len(time) == 2:
        clean_UTC_time.append('00' + time)       
    elif len(time) == 3:
        clean_UTC_time.append('0' + time)       
    elif len(time) == 1:
        clean_UTC_time.append('000' + time)       
    else:
        clean_UTC_time.append(time)       
      
clean_sunspot['hour'] = [int(time[0:2]) for time in clean_UTC_time]
clean_sunspot['minute'] = [int(time[2:4]) for time in clean_UTC_time]

# Prepare a new series in the clean_sunspot dataframe that 
# contains datetime objects
#The day month is not correct


sunspot_date_time = []

# When the df was subset, the indices came with.  They weren't reindexed...
# hence the clunky solution.
clean_index = clean_sunspot.index

for i in clean_index:
    sunspot_date_time.append(datetime.datetime(clean_sunspot.year[i], clean_sunspot.month[i], clean_sunspot.day[i], clean_sunspot.hour[i], clean_sunspot.minute[i]))

clean_sunspot['date_time'] = sunspot_date_time