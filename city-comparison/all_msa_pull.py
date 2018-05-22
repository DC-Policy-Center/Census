"""
Created
"""

import pandas as pd
import io, requests, time

def log_exception(message):
    current_time = time.strftime("%H:%M:%S",time.localtime())
    with open('run_log.txt','a') as log_file:
        log_file.write('Time: %s,  message: %s\n'%(current_time,message))

def empty_json(var):
    empty_json_variable = [[
            'NAME',
            str(var),
            'metropolitan statistical area/micropolitan statistical area'],
            [str(msa), 'NULL', 'NULL']
            ]
    return(empty_json_variable)

def msa_and_state_dict(msa_string):
    num_check = re.compile(r'[0-9]')
    if num_check.search(str(msa_string)):
        msa_dict = {msa_string:{'states':[],'area_type':'NA'}}
    else:
        comma_space_split = re.compile(r',\s')
        dash_split = re.compile(r'-')
        just_space_split = re.compile(r'\s')
        first_msa_split = comma_space_split.split(msa_string)
        msa_name = first_msa_split[0]
        msa_states_combined_with_area = first_msa_split[len(first_msa_split)-1]
        msa_states_combined = just_space_split.split(msa_states_combined_with_area,1)
        msa_state_list = dash_split.split(msa_states_combined[0])
        area_type = msa_states_combined[1]
        msa_dict = {msa_name:{'states':msa_state_list,'area_type':area_type}}
    return(msa_dict)


def pull_variable_data(yr,msa,var,key):
    metdiv_in_msa = "https://api.census.gov/data/%s/acs5?get=NAME,%s&for=metropolitan statistical area/micropolitan statistical area:%s&key=%s"%(str(yr),str(var),str(msa),str(key))
    d = requests.get(metdiv_in_msa)
    d_empty = empty_json(var)
    try: d_json = d.json()
    except:
        d_json = d_empty
        message = 'Empty json on msa %s, var %s\n\tURL %s\n\tResponse Code: %s'%(msa,var,metdiv_in_msa,d)
        log_exception(message)

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
tic = time.clock()

log_exception('Starting clock ...%s'%str(tic))
var_list = pd.read_csv('variable_list.csv')
#base_df = pull_variable_data(2015,'*','B01001_001E')
new_headers = []
initial_headers = ['NAME','metropolitan statistical area/micropolitan statistical area']
for h in initial_headers:new_headers.append(h)
for hh in list(var_list['name']): new_headers.append(hh)
with open('..\census_key.txt','r') as key_file:
    census_key = key_file.read()
census_key = census_key.rstrip('\n')
msa_dict = pd.read_csv('cbsa_list.csv')
#msa_list = msa_dict['CBSA']

msa_list = [
            47900,
            33100,
            37980,
            42660,
            12060,
            12580,
            14460,
            15380,
            16820,
            16980,
            19740,
            19820,
            28140,
            12420,
            46520,
            41860,
            41940,
            40900,
            41740,
            41180,
            33340,
            38300,
            38060
            ]

msa_index = 0
for msa in msa_list:

    j = 0

    if msa_index%10 == 0:
        time.sleep(5)
        print('Currently processing MSA# %s out of %s\n'%(str(msa_index),str(len(msa_list))))
   # if msa_index%100 == 0:
    #    time.sleep(120)
    for j in range(len(var_list)):
        var = var_list['variable'][j]
        pulled_df = pull_variable_data(2015,msa,var,census_key)
        #print('pulling the variable: %s \n    metric: %s'%(var,var_list['name'][j]))
        if j > 0:
            pulled_df.drop('metropolitan statistical area/micropolitan statistical area',axis = 1, inplace = True)
            com = pd.merge(base_df,pulled_df, on='NAME',how='inner')
            base_df = com
        else: base_df = pulled_df
        j+=1
    base_df.columns = new_headers
    if msa_index > 0 :
        full_df = full_df.append(base_df,ignore_index=True)
        msa_index +=1


    else:
        full_df = base_df
        msa_index +=1

toc = time.clock()
log_exception('Ending clock ...%s'%str(toc))
print('Time elapsed is: %s'%(str(toc-tic)))
log_exception('Ending program... time elapsed: %s'%str(toc-tic))
