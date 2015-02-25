# -*- coding: utf-8 -*-
"""
Created on Fri Feb 06 15:55:16 2015

@author: rdecrescenzo
"""

import re
import pandas as pd
import requests
import time
import csv
import matplotlib.pyplot as plt
import numpy as np

# change this to your pandora screen name!
screen_name = 'refivenine'
#####


set_list = set()
stations = 	requests.get('http://pandorasongs.oliverzheng.com/username/'+screen_name).json()
for station in stations['stations'][:]:
	stationID = station['stationId']
	print "on "+ station['stationName']
	i = 0
	songs = requests.get('http://pandorasongs.oliverzheng.com/station/'+stationID+'/'+str(i)).json()
	while songs['hasMore']:
		for song in songs['songs']:
			set_list.add( song['link'] )
		i += 1
		songs = requests.get('http://pandorasongs.oliverzheng.com/station/'+stationID+'/'+str(i)).json()
set_list = list(set_list)
len(set_list)


# get attributes of each song
new_set_list = []
all_atributes = set()
for song in set_list:
    print song
    site_text = requests.get('http://pandora.com'+song).text
    attributes = [r.strip().replace('<br>','') for r in re.findall('\\t\\t\\t[\w\s]*<br>\\n', site_text) if len(r) >= 9]
    if len(attributes):
        new_set_list.append( {'name':song, 'attributes':attributes} )
        [all_atributes.add(a) for a in attributes]
        


#create and save dataframe
rows = []
all_atributes =  list(all_atributes)
for n in new_set_list:
    rows.append( [n['name']] + [a in n['attributes'] for a in all_atributes] )
df = pd.DataFrame(rows, columns = ['name']+list(all_atributes))
# save
df.to_csv('songs.csv')

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import metrics


df = pd.read_csv('songs.csv')


# perform clustering with 4 clusters
song_cluster = KMeans(n_clusters=3, init='random')
song_cluster.fit(df.drop('name', axis=1))
y_kmeans = song_cluster.predict(df.drop('name', axis=1))

# get info on one cluster
for cluster_in_question in range(0,3):
    # get center of cluster
    song_cluster.cluster_centers_[cluster_in_question]
    # grab songs in dataframe that belong to this cluster
    print df[np.where(y_kmeans == cluster_in_question, True, False)]['name']
    # look at top five qualities in cluster
    print sorted(zip(df.columns[1:], song_cluster.cluster_centers_[cluster_in_question]), key=lambda x:x[1], reverse=True)[1:6]
 
metrics.silhouette_score(df.drop('name',axis=1), song_cluster.labels_, metric='euclidean')   
    
# perform k means with up to 9 clusters
k_rng = range(1,9)
est = [KMeans(n_clusters = k).fit(df.drop('name',axis=1)) for k in k_rng]



# calculate silhouette score
from sklearn import metrics
silhouette_score = [metrics.silhouette_score(df.drop('name',axis=1), e.labels_, metric='euclidean') for e in est[1:]]

# Plot the results
plt.figure(figsize=(7, 8))
plt.subplot(211)
plt.title('Using the elbow method to inform k choice')
plt.plot(k_rng[1:], silhouette_score, 'b*-')
plt.xlim([1,9])
plt.grid(True)
plt.ylabel('Silhouette Coefficient')
plt.plot(3,silhouette_score[1], 'o', markersize=12, markeredgewidth=1.5,
markerfacecolor='None', markeredgecolor='r')