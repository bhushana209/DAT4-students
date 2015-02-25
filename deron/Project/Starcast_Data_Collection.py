# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 23:24:09 2015

@author: deronhogans
"""

#NEXT STEPS
#Gather collection endpoints for Startup Sample for the following data:
    #Funds Raised
    # of Employees
    # of Press
#Read captured info into Dataframe
#Build valuation model (ex. #ofEmployee/FundsRaised > .5 = More Future funding?)


import requests
import json
import time
import pandas as pd

user_key = "2805358bf877c1b680623630187748a5"

# Get Funds Raised
def get_fundsraised(permalink):
    xparams = {"user_key" : user_key}
    FR_request = requests.get('https://api.crunchbase.com/v/2/organization/%s' % permalink, params=xparams)
    data= json.loads(FR_request.text)
    for item in data['data']['properties']:
        if item == 'total_funding_usd':
            return data['data']['properties'][item]

TheLeague_FR = get_fundsraised('the-league')
Lizhi_FR = get_fundsraised('lizhi')
CodeHS_FR = get_fundsraised("codehs")
Corp360_FR = get_fundsraised("corporate360")
Shocase_FR = get_fundsraised("shocase")

# Get # of Employees

def get_num_employees(permalink):
    xparams = {"user_key" : user_key}
    Employee_request = requests.get('https://api.crunchbase.com/v/2/organization/%s' % permalink, params=xparams)
    data= json.loads(Employee_request.text)
    for item in data['data']['properties']:
        if item == 'number_of_employees':
            return data['data']['properties'][item]

TheLeague_Num_Employees = get_num_employees('the-league')
Lizhi_Num_Employees = get_num_employees('lizhi')
CodeHS_Num_Employees = get_num_employees('codehs')
Corp360_Num_Employees = get_num_employees('corporate360')
Shocase_Num_Employees = get_num_employees('shocase')

# of Funding Rounds

def get_num_FR(permalink):
    xparams = {"user_key" : user_key}
    FR_num_request = requests.get('https://api.crunchbase.com/v/2/organization/%s' % permalink, params=xparams)
    data= json.loads(FR_num_request.text)
    for item in data['data']['relationships']['funding_rounds']['paging']:
        if item == 'total_items':
            return data['data']['relationships']['funding_rounds']['paging'][item]

TheLeague_Num_FR = get_num_FR('the-league')
Lizhi_Num_FR = get_num_FR('lizhi')
CodeHS_Num_FR = get_num_FR('codehs')
Corp360_Num_FR = get_num_FR('corporate360')
Shocase_Num_FR = get_num_FR('shocase')

# of Board Members/Advisors

def get_advisors(permalink):
    xparams = {"user_key" : user_key}
    getadvisor_request = requests.get('https://api.crunchbase.com/v/2/organization/%s' % permalink, params=xparams)
    data= json.loads(getadvisor_request.text)
    for item in data['data']['relationships']['board_members_and_advisors']['paging']:
        if item == 'total_items':
            return data['data']['relationships']['board_members_and_advisors']['paging'][item]

TheLeague_Advisors = get_advisors('the-league')
Lizhi_Advisors = get_advisors('lizhi')
CodeHS_Advisors = get_advisors('codehs')
Corp360_Advisors = get_advisors('corporate360')
Shocase_Advisors = get_advisors('shocase')

header_names = ['LeagueFundsRaised','LeagueEmployees','LeagueFundingRounds','LeagueAdvisors',\
           'LizhiFundsRaised','LizhiEmployees','LizhiFudningRounds','LizhiAdvisors',\
           'CodeHSFundsRaised','CodeHSEmployees','CodeHSFundingRounds','CodeHSAdvisors',\
           'Corp360FundsRaised','Corp360Employees','Corp360FundingRounds','Corp360Advisors',\
           'ShocaseFundsRaised','ShocaseEmployees','ShocaseFundingRounds','ShocaseAdvisors']
                                            
Starcast_DataFrame = pd.DataFrame(columns=header_names)

row = [TheLeague_FR, TheLeague_Num_Employees, TheLeague_Num_FR, TheLeague_Advisors,\
           Lizhi_FR, Lizhi_Num_Employees, Lizhi_Num_FR, 0,\
           CodeHS_FR, CodeHS_Num_Employees, CodeHS_Num_FR, 0,\
           Corp360_FR, Corp360_Num_Employees, Corp360_Num_FR, 0,\
           Shocase_FR, Shocase_Num_Employees, Shocase_Num_FR, 0]
                                            
Starcast_DataFrame.loc[len(Starcast_DataFrame)] = row

FundsRaised_Mean = TheLeague_FR + Lizhi_FR + CodeHS_FR + Corp360_FR + Shocase_FR/5

train = pd.DataFrame(data=X_train, columns=['LeagueFundsRaised', 'LizhiFundsRaised', 'CodeHSFundsRaised', 'Corp360FundsRaised', 'ShocaseFundsRaised']

