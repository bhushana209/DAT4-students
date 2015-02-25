# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 12:24:37 2015

@author: Jason
"""

import os
import csv
import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

xml_source_path = "..data/USPTO_zipfiles/"
xml_destination_path = "..data/formatted_xmls/"
csv_destination_path = "..data/csvs/"

xml_source_list = [xml_source_path + x for x in os.listdir(xml_source_path)[1:]]
csv_source_list = [xml_destination_path + x for x in os.listdir(xml_destination_path)[1:]]

csv.field_size_limit(sys.maxsize)


# reformat xmls to work with ElementTree
for xml in xml_source_list:
    text = '<patents>\n'
    with open(xml,'rU') as f:
       for line in f.readlines():
           if '<?xml' not in line and '<!DOCTYPE' not in line: 
               text += line
    text += '</patents>\n'
    with open(xml_destination_path + xml[-13:], 'wb') as g:
        g.write(text)

# assembles all applicants' names in one string
def applicantNames(patent):
    return_name = ''
    return_names = []
    for applicants in root[patent].findall('.//applicants'):
        apps = applicants.findall('.//applicant')
        for applicant in apps:
            lastname = applicant.findtext('.//addressbook/last-name') 
            firstname = applicant.findtext('.//addressbook/first-name')
            return_name = lastname + ', ' + firstname
            return_names.append(return_name)
    return return_names
 
# retrieves the patent assignee's organization name
def assigneeNames(patent):
    assignee_name = ''
    assignee_names = []
    if not len(root[patent].findall('.//assignee')):
        return 'None'
    for assignee in root[patent].findall('.//assignee'):
        name = assignee.findtext('.//orgname')
        assignee_name += ''.join(name)
        assignee_names.append(assignee_name)
    return assignee_names

# 3 functions to retrieve the patent assignee's address city, state, and country
def assigneeCity(patent):
    assignee_city = ''
    assignee_cities = []
    if not len(root[patent].findall('.//assignee')):
        return 'None'
    for assignee in root[patent].findall('.//assignee'):
        if assignee.findtext('.//city') != None:
            city = assignee.findtext('.//city').replace('\n', '')
        else:
            city = 'None' 
        assignee_city += ''.join(city)
    assignee_cities.append(assignee_city)
    return assignee_cities

def assigneeState(patent):
    assignee_state = ''
    assignee_states = []
    if not len(root[patent].findall('.//assignee')):
        return 'None'
    for assignee in root[patent].findall('.//assignee'):
        if assignee.findtext('.//state') != None:
            state = assignee.findtext('.//state').replace('\n', '')
        else:
            state = 'None'
        assignee_state = ''.join(state)
    assignee_states.append(assignee_state)
    return assignee_states

def assigneeCountry(patent):    
    assignee_country = ''
    assignee_countries = []
    if not len(root[patent].findall('.//assignee')):
        return 'None'
    for assignee in root[patent].findall('.//assignee'):
        if assignee.findtext('.//country') != None:
            country = assignee.findtext('.//country').replace('\n', '')
        else:
            country = 'None'
        assignee_country = ''.join(country)
    assignee_countries.append(assignee_country)
    return assignee_countries
        
# joins all of a patent's claim text into a single string
def claimCollect(patent):
    return_claims = ''
    for claim in root[patent].findall('.//claims'):
        return_claims += ''.join(claim.itertext()).replace('\n', ' ') + ' '
    return return_claims

# Extract all relevant patent data into one list
def csvExtract(patent):
    table_row = [root[patent].findtext('.//document-id/doc-number') , \
                 root[patent].findtext('.//invention-title'), \
                 root[patent].findtext('.//document-id/kind'), \
                 root[patent].findtext('.//document-id/date'), \
                 root[patent].find('.//application-reference').get('appl-type'), \
                 root[patent].findtext('.//application-reference//date'), \
                 root[patent].findtext('.//classification-national/main-classification'),\
                 len(root[patent].findall('.//references-cited/citation')), \
                 assigneeNames(patent), \
                 assigneeCity(patent), \
                 assigneeState(patent), \
                 assigneeCountry(patent), \
                 applicantNames(patent), \
                 len(root[patent].findall('.//applicants/applicant')), \
                 root[patent].findtext('.//abstract/*'), \
                 claimCollect(patent)]
    return table_row 

# Extract desired data from formatted xmls and write to individual csvs
for xml in csv_source_list[1:]:
    root = ET.parse(xml).getroot()
    patent_list = root.findall('us-patent-grant')
    patents_table = []
    for index, patent in enumerate(patent_list):
        try:
            patents_table.append(csvExtract(index))
        except:
            continue
    with open(csv_destination_path + xml[-13:-4] +'.csv', 'wb') as g:
        writer = csv.writer(g)
        writer.writerows(patents_table)
    root.clear()  

# Combine all csvs into one csv
with open("..data/patents.csv", 'wb') as g:
    writer = csv.writer(g, delimiter = ';')
    for csv_file in os.listdir(csv_destination_path)[1:]:
        print 'Processing', csv_file
        with open(csv_destination_path + csv_file, 'rU') as f:
            reader = csv.reader(f)
            for row in reader:  
                writer.writerow(row)
   


'''
A lot of stuff that didn't work.

for xml in csv_source_list[:5]:
    root = ET.parse(xml).getroot()
    patent_list = root.findall('us-patent-grant')
    patents_table = []
    patent_index = len(patent_list) - 1
    for patent in patent_list:
        patent = 0
        while patent < patent_index:
            patents_table.append(csvExtract(patent))
        patent += 1
    with open(csv_destination_path + xml[-13:], 'wb') as g:
        writer = csv.writer(g)
        writer.writerow(headers)
        writer.writerows(patents_table)
    root.clear() 

for xml in csv_source_list[:5]:
    root = ET.parse(xml).getroot()
    patent_list = root.findall('us-patent-grant')
    patents_table = []
    for patent in patent_list:
            table_row = [root[patent].findtext('.//document-id/doc-number'), \
                 root[patent].findtext('.//invention-title'), \
                 root[patent].findtext('.//document-id/kind'), \
                 root[patent].findtext('.//document-id/date'), \
                 root[patent].find('.//application-reference').get('appl-type'), \
                 root[patent].findtext('.//application-reference//date'), \
                 root[patent].findtext('.//classification-national/main-classification'),\
                 len(root[patent].findall('.//references-cited/citation')), \
                 assigneeNameAddress(patent)[0], \
                 assigneeNameAddress(patent)[1], \
                 applicantNames(patent), \
                 root[patent].findtext('.//abstract/*'), \
                 claimCollect(patent)]
        table.append(table_row)
    with open(csv_destination_path + xml[-13:], 'wb') as g:
        writer = csv.writer(g)
        writer.writerow(headers)
        writer.writerows(patents_table)
    root.clear() 
  
root[patent].get('.//application-reference')  
root[patent].find('.//application-reference[@appl-type=]')
parent_map = dict((c, p) for p in tree.getiterator() for c in p)


for grant in root.iterfind('../us-bibliograhpic-data-grant/publication-reference/document-id/doc-number'):
    print grant.tag, grant.text

for text in x.itertext():
            yield text
        for tail in x.itertext():
            yield tail

root[2250].findall('.//claims')

for x in root[patent].findall('.//claims'):
        i = x.findall('.//')
    for text in i:
        return ''.join(text.itertext()).replace('\n', '') 
          
def clCollect(patent):
    for x in root[patent].findall('.//claim'):
        return/yield ''.join(x.itertext()).replace('\n', '')
        
def clCollect(patent):
    for x in root[patent].findall('.//claim/claim-text*'):
        i = x.findall('[claim-text]*')
        for j in i:
            j = i.itertext()
            return ''.join(j)

This one works, but doubles the text of each claim for some reason.
def claimCollect(patent):
    return_claims = ''
    for claim in root[patent].findall('.//claims'):
        i = claim.findall('.//')
        for text in i:
            return_claims += ''.join(text.itertext()).replace('\n', '') + ' '
    return return_claims

[x.findall('.//claim') for x in root[2250].findall('.//claims')]

   for csv_file in os.listdir(csv_destination_path)[1:4]:
        print 'Processing', csv_file
        with open(csv_destination_path + csv_file, 'rU') as f:
            f.next()            
            csv.writer(g).writerows(f)
   
    writer = csv.writer(g, delimiter = ',')
    writer.writerow(headers)
    for csv_file in os.listdir(csv_destination_path)[1:2]:  
        print 'Processing', csv_file
        h = True
        with open(csv_destination_path + csv_file, 'rU') as f:
            if h:
                h = False
            else:
                f.next()
            for line in csv.reader(f, delimiter = ','):
                writer.writerow(line)
        

'''