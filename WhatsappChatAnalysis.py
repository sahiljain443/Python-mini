# -*- coding: utf-8 -*-
"""
Whatsapp Chat Analysis

"""
import re

#Open and read the file

full_file = open('C:/Users/ca33443/Desktop/Coding/Python/WhatsApp_Chat_with_Dav_2004.txt', 'r', encoding = 'utf8')

full_text = full_file.read(500)

print (full_text)

# Extract names - 
# Values between 'AM|PM - ' and ':'

def extract_names():
#    pattern = re.compile(r"[A|P]M\ \-(.*)\:")
#    result = pattern.search(full_text)
#    return (result.group(1))
    names = []
    match = re.findall(r'[A|P]M\ \-(.*)\:', full_text)
    
    for i in match:
        if i not in names:
            names.append(i)
    return(names)
    
print (extract_names())
    

# Count messages assuming that each message starts with a date in format dd/mm/yy
def message_counter():
    counter = 0
    
    pattern = re.compile(r'(\d|\d\d)\/(\d|\d\d)\/\d\d')
    
    matches = pattern.finditer(full_text)
    
    for match in matches:
        counter += 1
#        print(match)   
        
    return (counter)
print ('Total no. of messages based on RegEx: ' + str(message_counter()))

# Count words based on the number of 'space' characters
def word_counter():
    counter = 0
    for i in full_text:
        if (i == ' '):
            counter +=1
    return(counter)
print ('Total no. of words: ' + str(word_counter()))

print ('Avg no. of words per message: ' + str(word_counter()/message_counter()))

