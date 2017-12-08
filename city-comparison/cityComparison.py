# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 08:13:56 2017

@author: mwatson
"""

import pandas as pd
import io, requests


def pull_variable_data(yr,msa,state,var,key):
    #base_tract ="http://api.census.gov/data/%s/acs5?get=NAME,%s&for=tract:*&in=combined%20statistical%20area:%s"%(str(yr),str(var),str(state))
    #base_state = "http://api.census.gov/data/%s/acs1?get=NAME,%s&for=state:%s"%(str(yr),str(var),str(state))
    #base_csa = "	https://api.census.gov/data/%s/acs5?get=NAME,%s&for=metropolitan statistical area/micropolitan statistical area:%s&in=state:%s&key=%s"%(str(yr),str(var),str(msa),str(state),str(key))
    #base_csa = "	https://api.census.gov/data/%s/acs5?get=NAME,%s&for=Metropolitan Division:%s&in=state:%s&key=%s"%(str(yr),str(var),str(msa),str(state),str(key))
    #base_csa = "	https://api.census.gov/data/%s/acs1?get=NAME,%s&for=place:*&in=state:%s&key=%s"%(str(yr),str(var),str(state),str(key))
    
    metdiv_in_msa = "https://api.census.gov/data/%s/acs5?get=NAME,%s&for=metropolitan division:*&in=metropolitan statistical area/micropolitan statistical area:%s&key=%s"%(str(yr),str(var),str(state),str(key))
    
    d = requests.get(base_csa)

    d_json = d.json()
    d_list = []
    d_csv = []
    headers = []
    for i in range(len(d_json)):
        d_list_val = [d_json[i][0],d_json[i][1],d_json[i][2]]
        d_list.append(d_list_val)

        if i > 0:
            try:d_list_csv = d_json[i][0] + ',' + d_json[i][1]+','+d_json[i][2]
            except:'null'
            d_csv.append(d_list_val)

    df = pd.DataFrame(d_csv,columns=[d_json[0][0],d_json[0][1],d_json[0][2]])
    return df

var_list = pd.read_csv('variable_list.csv')
#base_df = pull_variable_data(2015,'*','B01001_001E')
new_headers = []
initial_headers = ['NAME','state']
for h in initial_headers:new_headers.append(h)
for hh in list(var_list['name']): new_headers.append(hh)
with open('census_key.txt','r') as key_file:
    census_key = key_file.read()
census_key = census_key.rstrip('\n')
msa_index = 0
msa_dict = {
            'msa':
                ['22744',
                 '33100'],
            'states':[
                    ['11','24','51'],
                    ['12']
                    ]}
msa_list = msa_dict['msa']

for msa in msa_list:
    state_list = msa_dict['states'][msa_index]
    state_index = 0
    for state in state_list:
        j = 0
        print(state)
        for j in range(len(var_list)):
            var = var_list['variable'][j]
            pulled_df = pull_variable_data(2015,msa,state,var,census_key)
            #print('pulling the variable: %s \n    metric: %s'%(var,var_list['name'][j]))
            if j > 0:
                pulled_df.drop('state',axis = 1, inplace = True)
                com = pd.merge(base_df,pulled_df, on='NAME',how='inner')
                base_df = com
            else: base_df = pulled_df
            j+=1
        base_df.columns = new_headers
        if state_index > 0 :
            full_df = full_df.append(base_df,ignore_index=True) 
    
        else: 
            full_df = base_df
            state_index +=1
    if msa_index > 0 :
        multi_df = multi_df.append(full_df,ignore_index=True)
        msa_index +=1

    else: 
        multi_df = full_df
        msa_index +=1
    
