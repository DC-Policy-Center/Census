# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:32:08 2017

@author: mwatson
"""

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

full = pd.read_csv('full_homeonwer_income_data.csv')

age_under_25 = []
age_25_44 = []
age_45_64=[]
age_65_plus=[]


