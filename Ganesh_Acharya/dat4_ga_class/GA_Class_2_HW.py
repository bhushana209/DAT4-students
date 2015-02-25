# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 16:04:02 2015

@author: ganeshacharya
"""
'''part1 - store the header in a list called 'header' and data in a list of 
lists called data'''
import csv
with open('drinks.csv','rU') as f:
    header=csv.reader(f).next()
    data=[row for row in csv.reader(f)]
    #print header
    #print data
#part 2 - Isolate the beer_servings in a list of integers called 'beers'
    beers=[rows [1] for rows in data]
    #print beers
#part 3 - Create separate lists of NA & EU beer servings: 'NA_beers','EU_beers'
    NA_beers=[]
    [NA_beers.append(rows[1]) for rows in data if rows [5]=='NA']    
    #print NA_beers   
    EU_beers=[]
    [EU_beers.append(rows[1]) for rows in data if rows [5]=='EU']  
    #print EU_beers
#part 4 - Calculate the average NA and EU beer servings to 2 decimals:'NA_avg', 'EU_avg'
    NA_beers_int=[int(values) for values in NA_beers]
    NA_avg=sum(NA_beers_int)/float(len(NA_beers_int))    
    #print "%.2f"%NA_avg
    EU_beers_int=[int(values) for values in EU_beers]
    EU_avg=sum(EU_beers_int)/float(len(EU_beers_int))    
    #print "%.2f"%EU_avg
#part 5 - Write a CSV file called 'avg_beer.csv' with two columns and three rows.
    new_file_values=[['continent','avg_beer'],['NA',NA_avg],['EU',EU_avg]]    
    with open('avg_beer.csv','wb') as f:
        csv.writer(f).writerows(new_file_values)
        