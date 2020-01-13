# -*- coding: utf-8 -*-
"""
Use REST API call to identify whether an application was accessed in duration (sec) 

@author: Sahil Jain
"""

import requests

def app_accessed(app_name):
    #send request and save response in response object
    response = requests.get(f'https://delta.goskope.com/api/v1/events?token=ea5fd39fbcb0dceca59868aae429f2d6&query=app%20eq%20%27{app_name}%27&type=application&timeperiod=86400')
    
    #extract data in json format
    r = response.json()
    
    # check if the data field in response object is blank
    if len(r['data'] ) == 0:
        fileHandler2.write(f'{app_name} : Not Accessed\n')
    else:
        fileHandler2.write(f'{app_name} : Accessed\n')

#open first file to read application names one at a time
fileHandler1 = open('C:/Users/ca33443/Downloads/test_domains.txt', 'r')

#open second file to write results
fileHandler2 = open('C:/Users/ca33443/Downloads/test_domains1.txt', 'a')

#Read lines from first file
lines = fileHandler1.readlines()

#Call funnction to check each application name
for app_name in lines:
    app_accessed(app_name.strip())

#Close the files
fileHandler1.close()
fileHandler2.close()