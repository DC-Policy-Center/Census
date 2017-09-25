import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
from ggplot import *

### data importing from cleaned csv ###
cleaned_income_data = pd.read_csv('homeowner_income_data.csv')
years                = cleaned_income_data['years']
years_ext            = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020];

income_0_to_49       = cleaned_income_data['income_0_to_49']
income_0_to_49_err   = cleaned_income_data['income_0_to_49_err']

income_50_to_74      = cleaned_income_data['income_50_to_74']
income_50_to_74_err  = cleaned_income_data['income_50_to_74_err']

income_75_to_any     = cleaned_income_data['income_75_to_any']
income_75_to_any_err = cleaned_income_data['income_75_to_any_err']


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

def fit_and_plot(x,y,options):
    A,B = curve_fit(f, x, y)[0] # your data x, y to fit
    values = []
    for i in range(len(years_ext)):
        values.append(A*years_ext[i] + B)
    if options == 1:
        plt.plot(years_ext,values,'red')
    elif options == 2:
        plt.plot(years_ext,values,'black')
    elif options == 3:
        plt.plot(years_ext,values,'blue')
#################### END METHOD DEFINTIONS ##################



#### Calculations ###
income_lower_0_to_49   = subtract_lists(income_0_to_49, income_0_to_49_err)
income_upper_0_to_49   = add_lists(income_0_to_49, income_0_to_49_err)

income_lower_50_to_74  = subtract_lists(income_50_to_74, income_50_to_74_err)
income_upper_50_to_74  = add_lists(income_50_to_74, income_50_to_74_err)

income_lower_75_to_any = subtract_lists(income_75_to_any, income_75_to_any_err)
income_upper_75_to_any = add_lists(income_75_to_any, income_75_to_any_err)


### Formatting figure ###
plt.figure()
ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_useOffset(False)  # This changes the x axis to show the year not sci-notation
plt.axis = years


############### Plotting error and lines of best fit ##############



############## 0 to 49 ################

plt.errorbar(years,income_0_to_49,color='red',yerr=income_0_to_49_err,fmt='o')
fit_and_plot(years,income_0_to_49,1)
fit_and_plot(years,income_lower_0_to_49,1)
fit_and_plot(years,income_upper_0_to_49,1)

############## 50 to 75 ###################

plt.errorbar(years,income_50_to_74,color='black',yerr=income_50_to_74_err,fmt='o')
fit_and_plot(years,income_50_to_74,2)
fit_and_plot(years,income_lower_50_to_74,2)
fit_and_plot(years,income_upper_50_to_74,2)



################# 75 to any ###############

plt.errorbar(years,income_75_to_any,color='blue',yerr=income_75_to_any_err,fmt='o')
fit_and_plot(years,income_75_to_any,3)
fit_and_plot(years,income_lower_75_to_any,3)
fit_and_plot(years,income_upper_75_to_any,3)


### Showing figure ####
#plt.show()



p = ggplot(cleaned_income_data,aes(x='years', y='income_75_to_any'))
p + geom_point()
p + geom_point(cleaned_income_data,aes('income_0_to_49'))


print(p)
