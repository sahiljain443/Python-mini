# -*- coding: utf-8 -*-
"""
Find number of strings in text using regular expression.

Created on Wed Jan  1 16:21:26 2020

@author: Sahil Jain
"""

import re

text_to_search = '''
abcd efg
4/5/19
3/4/18
5/3/18
'''

#Create RegEx for date format
pattern = re.compile(r'\d.\d.\d\d')

matches = pattern.finditer(text_to_search)

counter = 0

for match in matches:
    counter += 1
    
print (counter)
    
