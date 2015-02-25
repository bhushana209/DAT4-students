# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 18:35:19 2015

@author: ganeshacharya
"""

import statsmodels.formula.api as smf
lm=smf.ols(formula='Sales-TV', data=data).fit()
