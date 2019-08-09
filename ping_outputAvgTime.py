import schedule
import subprocess
import datetime
import time

def ping_host():
    # ping host www.google.com (5 times)
    # store results of ping in ping_output
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
    
    print ("I am working ...")

schedule.every(15).seconds.do(ping_host)

#schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
