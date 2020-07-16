#!usr/env/bin python3
interface = input("enter your interface>>")
 
mac = input("enter new mac>>")

print ("										")

print ("--------------------------------------------------------------------------")

import subprocess

subprocess.call("ifconfig " + interface + " down",shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + mac,shell=True)
subprocess.call("ifconfig " + interface + " up",shell=True)

print ("ONLY ON ROOTED DEVICE")
