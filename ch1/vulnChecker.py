"""
Author: Aleksa Zatezalo
Description: A vulnerability checker in python.
Date: June 8, 2023
"""

import sys
import os
import socket

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

def retBanner(ip, port):
    pass