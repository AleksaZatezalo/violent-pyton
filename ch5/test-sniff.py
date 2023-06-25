"""
Description: Sniffs packets and prints type to stdout.
Author: Aleksa Zatezalo
Date: June 24, 2023
"""

from scapy.all import *

def pktPrint(pkt):
    if pkt.haslayer(Dot11Beacon):
        print("[+] Detected 802.11 Becon Frame")
    if pkt.haslayer(Dot11ProbReq):
        print("[+] Detected 802.11 Probe Request Frame")
    if pkt.haslayer(TCP):
        print("[+] Detected TCP Packet")
    if pkt.haslayer(DNS):
        print("[+] Detected DNS Packet")

conf.iface = 'mon0'
sniff(prn=pktPrint)