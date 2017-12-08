import re
import pandas as pd
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

def add_key_to_msa(full_dict,msa_string,new_key,new_value):
    full_dict[msa_string].update({new_key:new_value})
    return(full_dict)
