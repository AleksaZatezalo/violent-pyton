from scapy.all import *

def pktPrint(pkt):
    if pkt.haslayer(Dot11Beacon):
        pass
    if pkt.haslayer(Dot11ProbReq):
        print("[+] Detected 802.11 Probe Request Frame")

    if pkt.haslayer(TCP):
        print("[+] Detected TCP Packet")
    if pkt.haslayer(DNS):
        print("[+] Detected DNS Packet")