## This script records the time elapsed between the request sent to salesforce.com and response received
## using Requests library of Python
## and records the output to a file get_Request_timeElapsed.txt


import requests
import time
import datetime
import schedule

def get_request_time_elapsed():
    
    gt = requests.get("https://www.salesforce.com", verify = False).elapsed.total_seconds()


    f = open ("getRequest_timeElapsed.txt", "a")
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') #current time of workstation
    
    print (st, '---https://www.salesforce.com---> ', gt, ' sec', file=f)

    f.close()    

    print ("I am working ...")
    
get_request_time_elapsed()

#schedule.every(15).seconds.do(get_request_time_elapsed)
schedule.every(1).minutes.do(get_request_time_elapsed)

while True:
    schedule.run_pending()
    time.sleep(1)
