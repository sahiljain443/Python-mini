#!/usr/bin/python

# run by crontab
# removes any files in /logs/ older than 10 days

import os, sys, time
from subprocess import call

def get_file_directory(file):
    return os.path.dirname(os.path.abspath(file))

now = time.time()
print ("Current Time"+now)
cutoff = now - (300)

files = os.listdir(os.path.join(get_file_directory(C:\TestPython), "logs"))
file_path = os.path.join(get_file_directory(C:\TestPython), "logs/")

print ("file"+files)
print ("file_path"+file_path)

for xfile in files:
    if os.path.isfile(str(file_path) + xfile):
        t = os.stat(str(file_path) + xfile)
        c = t.st_ctime
		print (c)
		
        # delete file if older than 10 days
		#if c < cutoff:
        #    os.remove(str(file_path) + xfile)