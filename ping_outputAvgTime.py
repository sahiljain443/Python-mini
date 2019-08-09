import subprocess
import datetime
import time


# ping host www.google.com (5 times)
# store results of ping in p1
ping_output = subprocess.Popen(['ping', '-c 5', 'www.google.com'], stdout=subprocess.PIPE).communicate()[0]

#extract min/avg/max/stddev time values of the ping
time_values = str(ping_output.split()[63])

#extract avg time value from p2
avg_time = time_values.split("/")[1]

# export output to a file output.txt
f = open ("output.txt", "a")
st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') #current time of workstation

print (st, '------> ', avg_time,'ms', file=f)

f.close()
