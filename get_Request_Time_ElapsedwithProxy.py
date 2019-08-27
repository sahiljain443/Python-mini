import requests
import time
import datetime
import schedule

def get_request_time_elapsedwithProxy():
    
    http_proxy = "http://10.2.227.30:8080"
    https_proxy = "https://10.2.227.30:8080"
  
    proxyDict = {
            "http"  : http_proxy,
            "https" : https_proxy,
            }
    
    gt = requests.get("https://www.salesforce.com", proxies=proxyDict, verify = False).elapsed.total_seconds()

    f = open ("getRequest_timeElapsedwithProxy.txt", "a")
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') #current time of workstation

    print (st, '---https://www.salesforce.com---> ', gt, ' sec', file=f)

    f.close()    

    print ("I am working ...")
    
get_request_time_elapsedwithProxy()

#schedule.every(15).seconds.do(get_request_time_elapsedwithProxy)
schedule.every(1).minutes.do(get_request_time_elapsedwithProxy)

while True:
    schedule.run_pending()
    time.sleep(1)
