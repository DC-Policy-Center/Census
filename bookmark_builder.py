
def clear_output():
    open('census_link_output.txt','w').close()
    return()

def write_link(census_variable,variable_description,series,year):
    base_url_5yr = 'https://factfinder.census.gov/bkmk/table/1.0/en/ACS/%s_%s/%s/0400000US11'%(year,series,census_variable)
    #https://factfinder.census.gov/bkmk/table/1.0/en/ACS/15_5YR/%s/0400000US11|multigeography
    url = base_url_5yr
    output_fmt = "<li><a href ='%s'>%s</a>: %s</li>\n"%(url,census_variable,variable_description)

    with open('census_link_output.txt','a') as output:
        output.write(output_fmt)
    output.close()

    return()

def test_run():
    variable_description_list = ['Median household income in the past 12 months (in 2015 inflation-adjusted dollars)',
                                    'Household size by vehicles avaliable',
                                    'Means of transportation to work by vehicles avaliable',
                                    'Population by race',
                                    'Populaton hispanic or latino origin by race']

    variable_list = ['B19013', 'B08201','B08141','B02001', 'B03002']

    i = 0
    for i in range(len(variable_list)):
        write_link(variable_list[i],variable_description_list[i],'5YR','15')
        i += 1

def import_variables(variable_csv):
# This is where I will point the reader to import variables and descriptions from a csv
    return()
def variable_input():
    variable_loop = True
    while variable_loop == True:
        variable = input('What census variable would you like to convert to a link for publication?:\n   ')
        description = input('\nWhat is the description of this variable that will be displayed on the publication?:\n   ')

        write_link(str(variable),str(description))

        continue_loop = input('Would you like to add another variable to the list(y/n)?:\n  ')
        continue_loop = str(continue_loop)
        if continue_loop.upper() == 'N' or  continue_loop.upper() == 'NO':
            variable_loop = False
            print('Thank you...')

def asking_loop():
    continue_asking = True
    while continue_asking == True:
        ask = input('What would you like to do?\n1)Input a variable\n2)Clear previous outputs\n3)Run the test\n')

        if ask == str(1):
            variable_input()
        elif ask == str(2):
            clear_output()
        elif ask == str(3):
            test_run()
        else:
            print('not a valid input')
        continue_asking_loop = input('Would you like to do anything else(y/n)?:\n  ')
        if continue_asking_loop.upper() == 'N' or  continue_asking_loop.upper() == 'NO':
            continue_asking = False
            print('Exiting...\nThank you...')

asking_loop()
