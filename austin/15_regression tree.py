# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 19:09:45 2015

@author: abrown1
"""

import numpy as np
import pandas as pd

vehicles = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT4/master/data/used_vehicles.csv").sort('price')

vehicles[vehicles.year < 2007]
vehicles_new = vehicles[vehicles.year >= 2007].sort('price')
vehicles_old = vehicles[vehicles.year < 2007].sort('price')

vehicles_new_lomi = vehicles_new[vehicles_new.miles < 40000]
vehicles_new_himi = vehicles_new[vehicles_new.miles > 40000]
vehicles_old_lomi = vehicles_old[vehicles_old.miles < 130000]
vehicles_old_himi = vehicles_old[vehicles_old.miles > 130000]

price1 = vehicles_new_lomi.price.mean()
price2 = vehicles_new_himi.price.mean()
price4 = vehicles_old_lomi.price.mean()
price5 = vehicles_old_himi.price.mean()