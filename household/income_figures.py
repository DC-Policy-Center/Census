import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


### hard-coded data ###
years                = [2010, 2011, 2012, 2013, 2014, 2015, 2016];
years_ext            = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020];

income_0_to_49       = [106514,108973,108394,105743,106661,103360,103692];
income_0_to_49_err   = [2041,2092,1943,2102,2163,1929,2097];

income_50_to_74      = [88259,96845,89392,92706,93903,93653,90337];
income_50_to_74_err  = [2102,2401,2140,2270,2130,2376,2381];

income_75_to_any     = [57615,62852,68876,73202,76814,84774,87212];
income_75_to_any_err = [1523,1596,1582,1686,1654,1659,1838];


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

def f(x, A, B): # this is your 'straight line' y=f(x)
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

### Formatting figure ###
plt.figure()
ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_useOffset(False)
plt.axis = years


### Plotting data with error terms ###
plt.errorbar(years,income_0_to_49,color='red',yerr=income_0_to_49_err,fmt='o')
plt.errorbar(years,income_50_to_74,color='black',yerr=income_50_to_74_err,fmt='o')
plt.errorbar(years,income_75_to_any,color='blue',yerr=income_75_to_any_err,fmt='o')



fit_and_plot(years,income_0_to_49,1)
income_lower = subtract_lists(income_0_to_49, income_0_to_49_err)
fit_and_plot(years,income_lower,1)

income_upper = add_lists(income_0_to_49, income_0_to_49_err)
fit_and_plot(years,income_upper,1)

############## 50 to 75 ###################
income_lower_50_to_74 = subtract_lists(income_50_to_74, income_50_to_74_err)
fit_and_plot(years,income_lower_50_to_74,2)

income_upper_50_to_74 = add_lists(income_50_to_74, income_50_to_74_err)
fit_and_plot(years,income_upper_50_to_74,2)

y_50_to_74 = income_50_to_74
fit_and_plot(years,income_50_to_74,2)

################# 75 to any ###############
fit_and_plot(years,income_75_to_any,3)

income_lower = subtract_lists(income_75_to_any, income_75_to_any_err)
fit_and_plot(years,income_lower,3)

income_upper = add_lists(income_75_to_any, income_75_to_any_err)
fit_and_plot(years,income_upper,3)


### Showing figure ####
plt.show()
