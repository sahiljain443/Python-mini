import subprocess

target = input("Enter an IP or Host to ping:")

p1 = subprocess.Popen(['ping', '-c 1', target], stdout=subprocess.PIPE).communicate()[0]

print (p1)