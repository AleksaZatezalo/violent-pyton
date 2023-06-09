"""
Description: Detect Fast Flux DNS attacks.
Author: Aleksa Zatezalo
Date: June 23, 2023
"""

from scapy.all import *

def dnsQRTest(pkt):
    if pkt.haslayer(DNSRR) and pkt.getlayer(UDP).sport == 53:
        rcode = pkt.getlayer(DNS).rcode
        qname = pkt.getlayer(DNSQR).qname
        if rcode == 3:
            print("[!] Name request lookup failed: " + qname)
        return (rcode == 3)
def main():
    unAnsReqs = 0
    pkts = rdpcap('domainFlux.pcap')
    for pkt in pkts:
        if dnsQRTest(pkt):
            unAnsReqs += 1
    print("[!] " + str(unAnsReqs) + ' Total Unanswered NAme Requests')

if __name__ == "__main__":
    main()