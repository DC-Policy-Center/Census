
def write_link(census_variable,variable_description):
    base_url_5yr = 'https://factfinder.census.gov/bkmk/table/1.0/en/ACS/15_5YR/%s/0400000US11'%(census_variable)
    #https://factfinder.census.gov/bkmk/table/1.0/en/ACS/15_5YR/%s/0400000US11|multigeography
    url = base_url_5yr
    output_fmt = "<li><a href ='%s'>%s</a>: %s</li>\n"%(url,census_variable,variable_description)

    with open('census_link_output.txt','a') as output:
        output.write(output_fmt)
    output.close()

    return()


variable_description_list = ['Median household income in the past 12 months (in 2015 inflation-adjusted dollars)',
                                'Household size by vehicles avaliable',
                                'Means of transportation to work by vehicles avaliable',
                                'Population by race',
                                'Populaton hispanic or latino origin by race']

variable_list = ['B19013', 'B08201','B08141','B02001', 'B03002']

i = 0
for i in range(len(variable_list)):
    write_link(variable_list[i],variable_description_list[i])
    i += 1
