import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import seaborn as sns
import mpld3 as mpl
sns.set(color_codes=True)
sns.set_style(style='white',)



### data importing from cleaned csv ###
cleaned_income_data = pd.read_csv('homeowner_income_data.csv')
years                = cleaned_income_data['years']
years_ext            = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020];

income_0_to_49       = cleaned_income_data['income_0_to_49']
income_0_to_49_err   = cleaned_income_data['income_0_to_49_err']

income_50_to_124      = cleaned_income_data['income_50_to_124']
income_50_to_124_err  = cleaned_income_data['income_50_to_124_err']

income_125_to_any     = cleaned_income_data['income_125_to_any']
income_125_to_any_err = cleaned_income_data['income_125_to_any_err']


################### method definitions #############
def add_lists(list_a, list_b):
    index = 0
    list_c = []
    for index in range(len(list_a)):
        list_c.append(list_a[index] + list_b[index])
    return list_c

def subtract_lists(list_a, list_b):
    index = 0
    list_c = []
    for index in range(len(list_a)):
        list_c.append(list_a[index] - list_b[index])
    return list_c

def f(x, A, B): # defining a line as f(x)
    return A*x + B

def fit_and_plot(x,y,options,fig):
    A,B = curve_fit(f, x, y)[0] # your data x, y to fit
    values = []
    for i in range(len(years_ext)):
        values.append(A*years_ext[i] + B)
    if options == 1:
        fig.plot(years_ext,values,'#E8272C')
    elif options == 2:
        fig.plot(years_ext,values,'#BECCDA')
    elif options == 3:
        fig.plot(years_ext,values,'#6D7D8C')
    print(A,B)
#################### END METHOD DEFINTIONS ##################



#### Calculations ###
income_lower_0_to_49   = subtract_lists(income_0_to_49, income_0_to_49_err)
income_upper_0_to_49   = add_lists(income_0_to_49, income_0_to_49_err)

income_lower_50_to_124  = subtract_lists(income_50_to_124, income_50_to_124_err)
income_upper_50_to_124  = add_lists(income_50_to_124, income_50_to_124_err)

income_lower_125_to_any = subtract_lists(income_125_to_any, income_125_to_any_err)
income_upper_125_to_any = add_lists(income_125_to_any, income_125_to_any_err)


### Formatting figure ###
plt.figure()
sns.despine()
ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_useOffset(False)  # This changes the x axis to show the year not sci-notation
plt.axis = years
sns.despine()

fig = plt.figure()
ax2 = plt.gca()
ax2.get_xaxis().get_major_formatter().set_useOffset(False)  # This changes the x axis to show the year not sci-notation
plt.axis = years

############### Plotting error and lines of best fit ##############



############## 0 to 49 ################

ax.errorbar(years,income_0_to_49,color='#E8272C',yerr=income_0_to_49_err,fmt='o')
fit_and_plot(years,income_0_to_49,1,ax)
#fit_and_plot(years,income_lower_0_to_49,1,ax)
#fit_and_plot(years,income_upper_0_to_49,1,ax)

############## 50 to 75 ###################

ax.errorbar(years,income_50_to_124,color='#BECCDA',yerr=income_50_to_124_err,fmt='o')
fit_and_plot(years,income_50_to_124,2,ax)
#fit_and_plot(years,income_lower_50_to_124,2,ax)
#fit_and_plot(years,income_upper_50_to_124,2,ax)



################# 75 to any ###############

ax.errorbar(years,income_125_to_any,color='#6D7D8C',yerr=income_125_to_any_err,fmt='o')
fit_and_plot(years,income_125_to_any,3,ax)
#fit_and_plot(years,income_lower_125_to_any,3,ax)
#fit_and_plot(years,income_upper_125_to_any,3,ax)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

### Showing figure ####

total_ownership = [252388,268670,266662,271651,277378,281787,281241]
total_ownership_err = [3730,3200,3138,3228,3304,3030,3152]



ax2.errorbar(years,total_ownership,color='#BECCDA',yerr=total_ownership_err,fmt='o')
fit_and_plot(years,total_ownership,2,ax2)
sns.despine()

#plt.show()



handles2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(handles2, labels2)

code = mpl.fig_to_html(fig)


