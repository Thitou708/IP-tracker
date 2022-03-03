#!/usr/bin/python3
# IP Tracker V1.0.0
# Code By: Thitou Kas ツ

print ("""\x1b[91;40m    ____            __             __                 
   /  _/___        / /__________ _/ /__________  _____
   / // __ \______/ __/ ___/ __ `/ //_/ ___/ _ \/ ___/
 _/ // /_/ /_____/ /_/ /  / /_/ / ,< / /__/  __/ /    
/___/ .___/      \__/_/   \__,_/_/|_|\___/\___/_/     
   /_/                                           V.2""") 

#imports:
import os
import sys
import json
import requests

#code:
ip_addr = input(">> Entrer L'adresse IP Box de la victime: ")

req1 = requests.get(f"http://ipinfo.io/{ip_addr}")
req2 = requests.get(f"http://ip-api.com/json/{ip_addr}")
req3 = requests.get(f"http://api.db-ip.com/v2/free/{ip_addr}")

resp1 = req1.text
resp2 = req2.text
resp3 = req3.text

print(resp3)
print(resp1)
print(resp2)

