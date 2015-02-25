import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#https://github.com/Kibrael/DAT4-students/blob/master/david/CourseProject/milwaukee2009.csv
#https://github.com/Kibrael/DAT4-students/blob/master/david/CourseProject/milwaukee2010.csv
#https://github.com/Kibrael/DAT4-students/blob/master/david/CourseProject/milwaukee2011.csv
#https://github.com/Kibrael/DAT4-students/blob/master/david/CourseProject/milwaukee2012.csv
#https://github.com/Kibrael/DAT4-students/blob/master/david/CourseProject/milwaukee2013.csv

#example Pandas code
#users = pd.read_table('../data/u.user', header=None, sep='|', names=u_cols, index_col='user_id', dtype={'zip_code':str})

mil_2009 = pd.read_csv('milwaukee2009.csv', sep='|')
#mil_2009 = pd.read_table('milwaukee2009.csv', sep='|', header=False)
#mil_2010 = pd.read_table('milwaukee2010.csv', sep='|', header=False)
#mil_2011 = pd.read_table('milwaukee2011.csv', sep='|', header=False)
#mil_2012 = pd.read_table('milwaukee2012.csv', sep='|', header=False)
#mil_2013 = pd.read_table('milwaukee2013.csv', sep='|', header=False)
#print mil_2009.head()
#m2009 = pd.DataFrame()
#del drinks['alcohol_mL']
drop_list = ['hoepastatus', 'applicantsex', 'coapplicantsex', 'count_name', 'state_name', 'respondend_name', 'agencycode', 'preapprovals', 'latitude', 'longitude',
'denialreason1', 'denialreason2', 'denialreason3']

for column in drop_list:
    del mil_2009[column]

print mil_2009.dtypes
print mil_2009.columns
print mil_2009.shape

#users[users.age < 20][['age', 'occupation']]        # select multiple columns
#users[(users.age < 20) & (users.gender=='M')]       # use multiple conditions