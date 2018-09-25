
import pandas as pd
import requests

msa_state_county_codes = pd.read_csv(".\\data\\input\\dc_area_counties.csv")

with open('..\census_key.txt','r') as key_file:
    census_key = key_file.read()
census_key = census_key.rstrip('\n')
    
def url_build(template = 'counties_in_states', year = '2015',survey = 'acs5', rest_call = "get=NAME,",variable ='B01001_001E',for_call = 'county', for_loc = '*', in_call = "state",in_loc = "11",api_key = ""):
    if template == 'counties_in_states':
        built_url = "https://api.census.gov/data/%s/%s?%s%s&for=%s:%s&in=%s:%s&key=%s"%(str(year),survey,rest_call,str(variable),for_call,str(for_loc),in_call,str(in_loc),str(api_key))
    return(built_url)


def shorthand_geo(shc):

    if shc == 'msa':
        lhc = 'metropolitan statistical area/micropolitan statistical area'   
    else:
        print('none')
    return(lhc)

'''
# "https://api.census.gov/data/"%s&for=metropolitan statistical area/micropolitan statistical area:%s&key=%s"%(str(yr),str(var),str(msa),str(key))
base_url = "https://api.census.gov/data/"
year = 2015
survey = 'acs5'


rest_call = "get=NAME,"
variable  =
for_call  =
for_loc = 
in_call   =
in_loc = 
api_key   = census_key
'''

year_list = ['2015','2014','2013','2012','2011','2010']
i = 0

d_csv_header = 'State,County,stateName,countyName'
for year in year_list:
    d_csv_header +=',data_'+ year
d_csv = [d_csv_header]
for i in range(len(msa_state_county_codes['stateCode'])):
    first_call = True
    for year in year_list:
        url = url_build(year = year,for_loc = str(msa_state_county_codes['countyCode'][i]).zfill(3),in_loc = str(msa_state_county_codes['stateCode'][i]),api_key=census_key)
        #print(url)
        data = requests.get(url)
        if first_call == True:
            state = data.json()[1][2]
            county = data.json()[1][3]
            stateName = msa_state_county_codes['state'][i]
            countyName = msa_state_county_codes['county'][i]
            pop_data = state + ',' + county + ','+ stateName + ',' + countyName 
            first_call = False
        var = data.json()[1][1]
        pop_data += ',' + var

    
    
    d_csv.append(pop_data)

    
    i+=1
    
with open('temp.csv','w') as f:
    for line in d_csv:
        f.write(line + '\n')
        
df = pd.read_csv('temp.csv')