import pandas as pd
import os

def year_of_files(short_year, year):
    data_location = './raw_data/e_%s/'%short_year
    template_location = './raw_data/t_%s/'%short_year
    iter = 1

    for filename in os.listdir(data_location):
        if filename.endswith('.txt'):
            input_file = filename.strip('.txt')
            try:
                singleFile(data_location,template_location, input_file, iter, short_year, year)
            except:
                print('\nFailed:    %s\n'%input_file)
                input('waiting for input...')
            iter +=1
    return;

def singleFile(data_location,template_location, file_name, iter,short_year, year):
    out_path = './cleaned_data/'

    data_file = file_name
    geo_template = '%s_SFGeoFileTemplate.xls'%year
    ext_in = '.txt'
    ext_out = '.csv'
    data_full = data_location+data_file+ext_in

    data = pd.read_csv(data_full)
    sequence = data.columns[4] #hard coded, test later
    #template_file = 'Seq%s.xls'%str(sequence).strip('0')
    #print('...Sequence:  %s\n...Stripped:  %s\n'%(sequence,sequence.strip('0')))
    template_file = 'Seq%s.xls'%str(iter)
    template_full = template_location+template_file

    template = pd.read_excel(template_full)
    data_with_headers = data


    geo_template_full = template_location+geo_template
    geo_header_template = pd.read_excel(geo_template_full)
    geo_with_headers= pd.read_csv('./raw_data/g%s1dc.csv'%year)



    headers = []
    for head in template.columns:
        headers.append(template[head][0])

    geo_headers = []
    for head in geo_header_template.columns:
        geo_headers.append(geo_header_template[head][0])

    data_with_headers.columns = headers
    geo_with_headers.columns = geo_headers
    data_with_headers_and_geo = data_with_headers

    data_with_headers_and_geo['Geographic Identifier']= geo_with_headers['Geographic Identifier']
    data_with_headers_and_geo['Area Name']= geo_with_headers['Area Name']

    data_with_headers.to_csv('%s%s_with_headers%s'%(out_path,data_file,ext_out))
    return;


year_list = ['16', '15', '14', '13', '12', '11', '10', '09']
for yr in year_list:
    short_year = yr
    print(short_year)
    year = '20%s'%short_year
    print('Running through...: %s\n'%year)
    year_of_files(short_year, year)
