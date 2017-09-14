import pandas as pd

data_location = './raw_data/'
template_location = './raw_data/t_16/'


out_path = './cleaned_data/'
data_file = 'e20161dc0003000'
geo_template = '2016_SFGeoFileTemplate.xls'
ext_in = '.txt'
ext_out = '.csv'
data_full = data_location+data_file+ext_in


data = pd.read_csv(data_full)
sequence = data.columns[4] #hard coded, test later
template_file = 'Seq%s.xls'%str(sequence).strip('0')
template_full = template_location+template_file
template = pd.read_excel(template_full)
data_with_headers = data


geo_template_full = template_location+geo_template
geo_header_template = pd.read_excel(geo_template_full)

geo_with_headers= pd.read_csv('./raw_data/g20151dc.csv')



headers = []



for head in template.columns:
    headers.append(template[head][0])

geo_headers = []
for head in geo_header_template.columns:
    geo_headers.append(geo_header_template[head][0])

data_with_headers.columns = headers
data_with_headers.columns = headers

geo_with_headers.columns = geo_headers


data_with_headers_and_geo = data_with_headers

data_with_headers_and_geo['Geographic Identifier']= geo_with_headers['Geographic Identifier']
data_with_headers_and_geo['Area Name']= geo_with_headers['Area Name']



data_with_headers.to_csv('%s%s_with_headers%s'%(out_path,data_file,ext_out))
