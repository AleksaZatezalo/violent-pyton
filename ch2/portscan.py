"""
Author: Aleksa Zatezalo
Date:  June 18, 2023
Description: A Port Scanner made in Python. Integrated with nmap.
"""

import optparse
from socket import *

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        print("[+] %d/TCP Open" % tgtPort)
        connSkt.close()
    except:
        print('[-]%d/TCP Closed' %tgtPort)

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s': Unkown host"%tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print ("\n[+] Scan Results for: " + tgtName[0])
    except:
        print("\n[+] Scan Results for: " + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port: ' + tgtPort)
        connScan(tgtHost, int(tgtPort))

### At Page 35 Application Banner Grabbing ###