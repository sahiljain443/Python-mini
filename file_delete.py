import os
import glob
file_list=glob.glob("C:\TestPython\*.txt")

for file in file_list:
	os.remove(file)
