"""
Author: Aleksa Zatezalo
Description: A vulnerability checker in python.
Date: June 8, 2023
"""

import sys
import os
import socket

def retBanner(ip, port):
    """
    Takes the ip, ip of a remote server and it's respective port, port.
    Returns the banner running at the location.
    """
    
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner, filename):
    """
    Checks the banner, banner, of a remote server against a database of 
    vulnerable services, filename. Prints if server is vulnerable. No returns.
    """

    f = open(filename, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print("[+] Server is vulnerable " + banner.strip('\n'))

def main():

    # Check vuln file
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        if not os.path.isfile(file_name):
            print('[-] ' + file_name + ' does not exist.')
            exit(0)
        if not os.access(file_name, os.R_OK):
            print('[-] ' + file_name + ' access denied.')
            exit(0)
        print('[+] Reading Vulnerabilities From: ' + file_name)
    
    if len(sys.argv) != 2:
        print('[-] Usage: ' + str(sys.argv[0]) + '<vuln filename>')
        exit(0)

    portList = [21, 22, 25, 80, 110, 443]
    for port in portList:
        banner = retBanner(sys.argv[1], port)
        if banner:
            print("[+] " + sys.argv[1] + " : " + banner)
            checkVulns(banner, file_name)