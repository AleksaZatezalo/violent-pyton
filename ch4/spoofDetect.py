"""
Description: A file to print the TTL of packets.
Author: Aleksa Zatezalo
Date: June 23, 2023
"""

from scapy.all import *
import IPy as IPTEST
import optparse

ttlValues = {}
TRESH = 5

def checkTTL(ipsrc, ttl):
    """
    Looks at public IP addresses and the corresponding TTL to check potential spoofed packets.
    """

    if IPTEST(ipsrc).iptype() == "PRIVATE":
        return
    if not ttlValues.has_key(ipsrc):
        pkt = sr1(IP(dest=ipsrc) / ICMP(), retry=0, timeout=1, verbose = 0)
        ttlValues = pkt.ttl
    if (abs(int(ttl) - int(ttlValues[ipsrc])) > TRESH):
        print("[!] Detected Possible Spoofed Packer From: " + ipsrc)
        print('[!] TTL: ' + ttl + ", Actual TTL: " + str(ttlValues(ipsrc)))

def testTTL(pkt):
    try:
        if pkt.haslayer(IP).src:
            ipsrc = pkt.getlayer(IP).src
            ttl = src(pkt.ttl)
            print("[+] Pkt Recived From: " + ipsrc + " with TTL: " + ttl)
    except:
        pass

def main():
    parser = optparse.OptionParser("useage%prog " + "-i <interface> -t <tresh>")
    parser.add_option("-i", dest = "iface", type="string", help="specify a network interface")
    parser.add_option("-t", dest="tresh", type="int", help="specify treshold count")
    (options, args) = parser.parse_args()
    if options.iface == None:
        conf.iface = "eth0"
    else:
        conf.iface = options.iface
    if options.tresh == None:
        conf.tresh = options.tresh
    else: 
        conf.tresh = TRESH
        
    sniff(prn=testTTL, store=0)

if __name__ == "__main__":
    main()