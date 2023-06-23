"""
Description: A tool used to detec DDOS attacks. Written in python.
Author: Aleksa Zatezalo
Date: June 23, 2023
"""

# Imports
import dpkt
import socket
import optparse

# Global Variables
TRESH = 10000 # Treshold for DDoS attacks

# Functionality
def findHivemind(pcap):
    """
    Analyzes pcap files, pcap, to find the command `!lazer` sent to port 6667.
    """
    
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip)
            dst = socket.inet_ntoa(ip)
            tcp = ip.data
            dport = tcp.dport
            sport = tcp.sport

            if dport == 6667:
                if "!laser" in tcp.data.lower():
                    print("[!] DDoS Hivemind issued by: "+ src)
                    print("[+] Target CMD: " + tcp.data)
        except:
            pass


def findAttack(pcap):
    """
    Analyses a pcap file, pcap, and identifies a DDoS attack if the number of requsts are above TRESH.
    """
    
    pkCount = {}
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport
            if (dport == 80):
                stream = src + ":" + dst
                if pkCount.has_key(stream):
                    pkCount[stream] += 1
                else:
                    pkCount = 1
        except:
            pass

    for stream in pkCount:
        pksSent = pkCount[stream]
        if pksSent >= TRESH:
            src = stream.split(":")[0]
            dst = stream.split(":")[1]
            print("[+] " + src + " attacked " + dst + " with " + pksSent + " packets.")

def findDownload(pcap):
    """
    Analyses pcap files to see if Low Orbit Ion Cannon was downloaded.
    """

    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            http = dpkt.http.Request(tcp.data)
            if http.method == 'GET':
                uri = http.uri.lower()
                if '.zip' in uri and 'loic' in uri:
                    print('[!] ' + src + ' Downloaded LOIC.')
        except:
            pass
def main():
    
    # Specify and Open PCAP Files
    parser = optparse.OptionParser('usage%prog -p <pcapfile>')
    parser.add_option('-p', dest='pcapFile', type='string', help="Specify pcap filename")
    (options, args) = parser.parse_args()
    if options.pcapFile == None:
        print(parser.usage)
        exit(0)
    pcapFile = options.pcapFile
    f = open(pcapFile)
    pcap = dpkt.pcap.Reader(f)

    # Test for LOIC
    findDownload(pcap)
    findHivemind(pcap)
    findAttack(pcap)

if __name__ == "__main__":
    main()