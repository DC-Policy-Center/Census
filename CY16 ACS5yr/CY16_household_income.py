"""
Created on Thu Dec  7 10:41:24 2017

@author: mwatson
"""

import pandas as pd


# I cut 2009 from the list because the tracts changed in 2010, it is simplifying for now
year_list =["10","11","12","13","14","15","16"]
full_year_list=["2010","2011","2012","2013","2014","2015","2016"]
year_index = 0
i = 0

var_string = 'Married-couple families; Estimate; Median income (dollars)'


for year in year_list:
    print(year)
    if year_index == 0: 
        big_df = pd.read_csv("./data/ACS_%s_5YR_S1901_with_ann.csv"%year_list[0])      
    else: 
        big_df = pd.concat([big_df,pd.read_csv("./data/ACS_%s_5YR_S1901_with_ann.csv"%year)],axis=1)
    year_index +=1


year_index = 0
geography = big_df['%s_Id2'%"2010"]
geo_df = pd.DataFrame(geography)
for year in full_year_list:
    census_variable = '%s_%s'%(year,var_string)
    data = big_df[census_variable]
    if year_index == 0:
        var_df = pd.DataFrame(data)
        int_df = pd.concat([geo_df,var_df],axis=1)
        full_df = int_df

    else:
        full_df = pd.concat([full_df,data],axis=1)
    year_index += 1


