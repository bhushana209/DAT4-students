# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 09:58:29 2015

@author: Jason
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


headers = ['grant_doc_num', # assigned patent number
'invention_title', 
'grant_kind', # type of patent granted
'grant_date', # when patent was granted
'appl_type', # type of patent applied for
'appl_date', # date of patent application
'main_class', # main US government classification of patent
'num_refs', # number of references cited by the patent applicant and examiners
'assignee_org', # holder of patent
'assignee_city',    
'assignee_state',
'assignee_country',
'applicant_name', # name of inventor(s)
'num_applicants', # number of applicants
'abstract', # synopsis of patent claims
'claims'] # explanation of patent   

date_cols = ['grant_date', 'appl_date']

patents = pd.read_csv('/Users/Jason/Documents/DataScience/DAT4-students/jason/final_project/data/patents.csv', 
                      sep = ';', header = None, names = headers, 
                      parse_dates = date_cols, encoding = 'utf_8')

patents.info()

# Unicode value dict for extraneous characters in text fields
extraneous_table = dict.fromkeys(map(ord, '[].,"\'();'), None)

# List of lists of unicode chars for unnecessary words at the end of company names
company_end_table = []
company_end_list = ['Co', 'co', 'Inc', 'GmbH', 'SA', 'S A', 'BV', 'Ltd', \
                    'Corporation', 'Corp', 'Limited', 'Company', \
                    'SPA', 'Mfg', 'LLC', 'LLP', 'AS', 'AG', 'Aktiengesellschaft', \
                    'SAS', 'KG', 'NV', 'SpA', 'AB', 'SL', 'ASA', 'SRL', 'Ltda', \
                    'PLC', 'Plc', 'a/s']
for ending in company_end_list:
    ending_chars = list(ending)
    ending_codes = [ord(char) for char in ending_chars]
    company_end_table.append(ending_codes)

# Function to create a clean list of unique values in assignee text fields
cities = []
states = []
countries = []
companies = []

def clean_text(df_column, list_name):
    value_set = set()
    for value in df_column:
        value_set.update(x for x in value.split(','))
    value_list = [val.translate(extraneous_table) for val in list(value_set)]
    new_value_list = []
    for v in value_list:
        if not v == '' and ord(v[0]) == ord(' '):
            new_value_list.append(v.lstrip())
        else:
            new_value_list.append(v)
    new_value_list = list(sorted(set(new_value_list)))
    [list_name.append(name) for name in new_value_list]
    return list_name

clean_text(patents.assignee_city, cities)
clean_text(patents.assignee_state, states)
clean_text(patents.assignee_country, countries)
clean_text(patents.assignee_org, companies)


companies = set()
for company in patents.assignee_org:
    companies.update(comp for comp in company.split(','))
companies = list(sorted(set(companies)))

clean_companies = [company.translate(extraneous_table) for company in companies]
clean_companies = list(sorted(set(clean_companies)))




        






for elem in company_end_list:
    







for company in clean_companies:
    split_company = company.split()
    for elem in split_company[-2:]:
        ['' for elem in split_company[-2:] if any(elem in split_company[-2:] \
        for elem in company_end_list)]
    company = company.join(split_company[:])

patents.columns

dupes = patents.duplicated(cols = 'assignee_org')
dupes.value_counts()
patents.assignee_org.get(806484)

patents['time_elapsed'] = patents.grant_date - patents.appl_date
patents['time_elapsed'].astype('timedelta64[D]')
patents['time_elapsed'].apply(lambda x: x / np.timedelta64(1, 'D'))

patents.boxplot(column = 'time_elapsed', by = 'appl_type')



'''
patents['time_delt'] = [str(x).split() for x in patents['time_elapsed']]
def days_extract(index):
    days = None    
    for string in index:
        days = int(index[0])
    return days

patents['time_delt'].applymap(days_extract)

patents.main_class.value_counts().plot(kind = 'bar')

    
clean_values = [val.translate(extraneous_table) for val in list(sorted(value_set))]
[list_name.append(v) for v in clean_values]
return list_name

holding_set = sorted(holding_set)
holding_list = [name.translate(extraneous_table) for name in list(holding_set)]
holding_list = sorted(holding_list)
list_name.append(holding_list)
return list_name

cities = set()
for city in patents.assignee_city:
    cities.update(town for town in city.split())
cities = sorted(cities)
[x.strip('"[]\',"') for x in cities]
print cities[-16].decode('unicode_escape')

states = set()
for state in patents.assignee_state:
    states.update(st for st in state.split())
states = list(sorted(states))

clean_states = [state.translate(extraneous_table) for state in states] 
clean_states = set(clean_states)

countries = set()
for country in patents.assignee_country:
    countries.update(c for c in country.split())
countries = sorted(countries)

companies = set()
for company in patents.assignee_org:
    companies.update(comp for comp in company.split(','))
companies = list(sorted(companies))

clean_companies = [company.translate(extraneous_table) for company in companies]
clean_companies = list(set(clean_companies))
'''