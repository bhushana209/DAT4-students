# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 11:47:59 2015

@author: Akshay
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 15:56:03 2015

@author: Akshay
"""

#Import Packages
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns
import time         
import re           
from pprint import pprint
from BeautifulSoup import BeautifulSoup
import urllib2 as urllib

#Interacting with GTD Databse 
import os
os.chdir("/Users/Akshay/Documents/Dropbox/Work/Data Science")
print os.getcwd()

#importing Global Terrorism Database and Seeing Headers
gtd = pd.read_csv('GTD.csv', sep=",", index_col=False, dtype={'country':str,'targteyp1':int})
print gtd.columns


#remove duplicates of Terrorist Incidents - particularly important because often-times incident is "double counted" If bombs went of in two locations, etc. 
gtd.duplicated().sum()    
gtd.drop_duplicates()     


"""Obviously there are a lot of variables here so I'll list down some of the important ones I'll be workingw ith

doubterr = categorical, doubt whether incident was actually a terrorism attack 1="Yes" 0="No. I'll want to remove these 
country= categorical, I'll want to remove non-Western countries and countries without established and mature stock markets
attacktype1: categorical, I want to remove "unknown" and "unarmed assault" attack types from this as well
success: categorical 1/0. Obviously will help if I want to remove these
targtype1: categorical, 1-22, tells us what attack was targeting (telecomm, utilities, transportation, )
tarsubtype1: categorical, 1-105 further type (gas/oil/construction/bank, etc.)
gname: perpetrator group 
nkill: total number of fatalities
nwound: total number injured
propertydamage: categorical, 1/0
value of property damage: numeric, in USD

"""

#Now I want to filter data by some conditions in pandas
#limit by OECD countries
#limit date past 1995
#we'll also remove attacks which had 'unkown' weapons or were unarmed terror attacks (whatever the fuck that means)
#this still has 1638 values so we might have to reduce the dataset further dependent on 
OECD_countries = ['United States', 'Austria', 'Australia', 'Belgium', 'Canada', 'Denmark', 'Finland', 'France', 'Germany', 'Hong Kong', 'Iceland', 'Israel', 'Italy', 'Japan', 'Luxemborg','Netherlands', 'New Zealand','Norway','Portugal','Singapore','South Korea','Spain', 'Spain', 'Sweden', 'Switzerland', 'United Kingdom']
US_countries = ['United States']
gtdr = gtd[(gtd.country_txt.isin(US_countries)) & (gtd.iyear>1980) & (gtd.attacktype1!=8) &(gtd.targtype1!=5)]
#important to see what these attacks targeted  and how that is  distributed

#let's plot that
sns.set(style='whitegrid', palette="deep", font='Arial')

fig = plt.figure()

fig = plt.figure()
y =  gtdr.targtype1.value_counts()
x = gtdr.targtype1.unique()

targtype1_labels = ['','Business', 'Govt', 'Police', 'Military', '', 'Airlines', 'Diplomatic','Educational','Food/Water','Media', 'Maritime','NGO', '', 'Property', 'Religious','Telecomm', 'Militias', 'Tourists', 'Transportation', '', 'Utilities', 'PolParty']


plt.xlabel('Target Type')
plt.ylabel('Frequency')
plt.title('U.S. Terrorist Attacks by Target Type, 1990-2014', fontsize="18")
plt.xticks(range(23),targtype1_labels, rotation='vertical')
plt.xlim((0,23))
plt.tight_layout()
plt.bar(x,y, align='center')



#IGNORE - PRACTICING USING DATE-TIME
#from datetime import datetime
#from datetime import timedelta
#from datetime import date
#
#s = str(dateutil.parser.parse("February 16th 2014"))
#print s
#
#s = "August 16th, 2012"
#d = datetime.strptime(s, "%B %dth, %Y")
#print(d)
#
#
#today = date.today()
#yesterday = today - timedelta(days=1)




#IGNORE- quick tutorial on how to get create unique variable names from arguments of a funciton
#unique_name = "%s-%s-%s" % (ticker, str(timedelta), unit_of_time)
#    print unique_name

#mydict = {}
#mydict['akey'] = 55
#mydict['another key'] = Object()
#var = "AAA"
#foo = {}
#mydict[var] = foo
 


#FinancialData

import datetime
import pandas as pd
import pandas.io.data
from pandas import Series, DataFrame

#an example using Apple stock
aapl = {}
aapl = pd.io.data.get_data_yahoo('AAPL', 
                                 start=datetime.datetime(2007, 10, 1), 
                                 end=datetime.datetime(2008, 1, 1))
                                 
aapl = aapl.to_dict()                                

for key in aapl: 
    print aapl['Low']
                                 


aapl['Open']

apple_data_dict = {}
apple_data_dict['sample'] = aapl
pprint(apple_data_dict)

apple_data_dict['sample']['Close']


''''

======EXPLANATION OF FUNCTION=======
A lot of this project will be creating quick and dirty data visualizations.
Is a particular industry's index effected over the course of a day/week/month?
And what about specific subsections of industries?

Because the GTD dataset sorts attack by 23 industries and 80+ subindustries, it's
easy to create small dataframes from the larger dataset. 

After that, I want to quickly pull data on the attacks within those smaller dataframes. 

To do that, I wanted to create a function which quickly pulled financial data
based on the days the attacks occured. 

The function takes five arguments:
-df: the dataframe of terrorist attacks
-ticker: the relevant ticker (so for the U.S. airlines index 'DJUSAR')
-timedelta and unit_of_time: the time period after the attack I want to look attack
    (timedelta takes integer while unit_of_time specifies whether we're working with 
    months, weeks, days)
-industry: denotes the industry we're working with


====PSEUDOCODE=======
given a dataframe of terrorist attacks, a stock ticker, a given period of time, and the name of the industry
    go through each attack in the dataframe
    pull the financial data for the given period of time after the attack
    add the financial data for that attack into a dictionary
    

ALSO: for the purpose of creating quick data visualizations I can look at this data clearly,
each dictionary should have a unique name based on the arguments I give it. 
That way, it's there's a standard form for creating data visualizations




 
 dictionary[key] = dictionary.get(key, []) + [val]


''''

'''FUNCTION'''

gtdr_USairlines = gtdr[(gtdr.targsubtype1 == 42)]



financial_effect = {}

def stockdata(df, ticker, timedelta, unit_of_time, industry):
    unique_dataframe_name = "%s_%s_%s_%s" % (industry, ticker, timedelta, unit_of_time)
#    stockdata_columns = range(timedelta)
#    stockdata= pd.DataFrame(data=np.zeros((0,len(stockdata_columns))), columns=stockdata_columns)   
    
    for attack in df.iterrows():
        start_time = datetime.datetime(int(attack[1][1]), int(attack[1][2]), int(attack[1][3]))
        end_time = start_time + datetime.timedelta(days = timedelta)
        
        finance_data_raw = pd.io.data.get_data_yahoo(str(ticker),
                                       start=datetime.datetime(int(attack[1][1]), int(attack[1][2]), int(attack[1][3])),
                                       end=start_time + datetime.timedelta(days = timedelta))
        finance_data_raw = finance_data_raw.to_dict()                                
        financial_effect[unique_dataframe_name] = financial_effect.get(unique_dataframe_name, []) + [finance_data_raw]
        
        print financial_effect

stockdata(gtdr_USairlines, 'AAPL', 20, 'days', 'airlines')




y = financial_effect['airlines_AAPL_20_days'][0]['Close'].values()





len(y)
len(x)







y = []
for i in range(4):
    y = []
    for key in sorted(financial_effect['airlines_AAPL_20_days'][i]['Close']):
        #x.append(key)
        y.append(financial_effect['airlines_AAPL_20_days'][i]['Close'][key])#.strftime('%D'))
    x = range(len(y))    
    plt.plot(x,y)

for key in financial_effect['airlines_AAPL_20_days'][0]['Close'].keys():
    x.append(key)#.strftime('%D'))
    

plt.plot(x,y)



for key in financial_effect['airlines_AAPL_20_days'][0]['Volume'].keys():
    print key.strftime('%D')


import datetime
print(
    datetime.datetime.fromtimestamp(
        int("1284101485")
    ).strftime('%Y-%m-%d %H:%M:%S')
)

#Messin' with Matplotlib

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker



datafile = cbook.get_sample_data('aapl.csv', asfileobj=False)
print ('loading %s' % datafile)
r = mlab.csv2rec(datafile)

r.sort()
r = r[-30:]  # get the last 30 days


# first we'll do it the default way, with gaps on weekends
fig, ax = plt.subplots()
ax.plot(r.date, r.adj_close, 'o-')
fig.autofmt_xdate()


N = len(r)
ind = np.arange(N)  # the evenly spaced plot indices

def format_date(x, pos=None):
    thisind = np.clip(int(x+0.5), 0, N-1)
    return r.date[thisind].strftime('%Y-%m-%d')

fig, ax = plt.subplots()
ax.plot(ind, r.adj_close, 'o-')
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
fig.autofmt_xdate()

plt.show()

####

'''''
Goes down, goes up, or stays the same? Did it go down or stay the same?

-Did it go down by a significant amount
-volatility measure increased?

-binary variable of decrease or not decrease
-logistic regression
-decision trees
-date greater than september 11th 2001
