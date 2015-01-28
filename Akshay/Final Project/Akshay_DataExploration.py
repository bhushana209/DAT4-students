# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 15:56:03 2015

@author: Akshay
"""

#Import Packages
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests
import json



#Interacting with GTD Databse 
import os
os.chdir("/Users/Akshay/Documents/Dropbox/Work/Data Science")
print os.getcwd()

#importing Global Terrorism Database and Seeing Headers
gtd = pd.read_csv('GTD.csv', sep=",", index_col="eventid", dtype={'country':str})
print gtd.columns


#remove duplicates of Terrorist Incidents - particularly important because often-times incident is "double counted" If bombs went of in two locations, etc. 
gtd.duplicated().sum()    
gtd.drop_duplicates()     


'''Obviously there are a lot of variables here so I'll list down some of the important ones I'll be workingw ith

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

''''

#Now I want to filter data by some conditions in pandas
#limit by OECD countries
#limit date past 1995
#we'll also remove attacks which had 'unkown' weapons or were unarmed terror attacks (whatever the fuck that means)
#this still has 1638 values so we might have to reduce the dataset further dependent on 
gtd = pd.read_csv('GTD.csv', sep=",", index_col="eventid", dtype={'country_txt':str})

OECD_countries = ['United States', 'Austria', 'Australia', 'Belgium', 'Canada', 'Denmark', 'Finland', 'France', 'Germany', 'Hong Kong', 'Iceland', 'Israel', 'Italy', 'Japan', 'Luxemborg','Netherlands', 'New Zealand','Norway','Portugal','Singapore','South Korea','Spain', 'Spain', 'Sweden', 'Switzerland', 'United Kingdom']
gtdr = gtd[(gtd.doubtterr!=1) & (gtd.country_txt.isin(OECD_countries)) & (gtd.iyear>1997) & (gtd.attacktype1!=8) & (gtd.attacktype1!=6) &(gtd.targtype1!=5)& (gtd.targtype1!=13) & (gtd.targtype1!=20)]


#important to see what these attacks targeted  and how that is  distributed

#let's plot that
fig = plt.figure()
x =  gtdr.targtype1.unique()
y = gtdr.targtype1.value_counts.sort()
targtype1_labels = ['Business', 'Govt', 'Police', 'Military', 'Airlines','Diplomatic','Educational','Food/Water','Media','Maritime','NGO','Property', 'Religious','Telecomm', 'Militias','Tourists', 'Transportation', 'Utilities', 'PolParty']



plt.xlabel('Target Type')
plt.ylabel('Frequency')
plt.title('Attacks by Target Type')
plt.xticks(x, targtype1_labels, rotation='vertical')
plt.ylim((0,800))
plt.xlim((0,23))
plt.bar(x,y, align='center')
gtd.targtype1.value_counts().plot(kind='bar')


#I should have tried to use the Bloomberg API and got Brandon's help, but we had difficulty installing it and he suggested I use Google Finance


