"""
Description: A script to print the direction of network traffic.
Author: Aleksa Zatezalo
Date: June 23, 2023
"""

import dpkt, socket, pygeoip, optparse
gi = pygeoip.GeoIP('/opt/GeoIP/GEO.dat')


def retGeoStr(ip):
    """
    Takes an IP address, ip, and prints its geo-location to STDOUT.
    """

    try:
        rec = gi.record_by_name(ip)
        city = rec["city"]
        country = rec["country_code3"]
        if (city!=""):
            geoLoc = city +", "+country
        else: 
            geoLoc = country
        return geoLoc
    except:
        pass 


def printPcap(pcap):
    """
    Takes a packet, pcap, and prints the direction within which it is traveling
    to STDOUT.
    """
    
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print("[+] Src: " + retGeoStr(src) + "--> Dst: " + retGeoStr(dst))
        except:
            pass
        
def main():
    parser = optparse.OptionParser('usage%prog -p <pcapfile>')
    parser.add_option('-p', dest='pcapFile', type='string', help="Specify pcap filename")
    (options, args) = parser.parse_args()
    if options.pcapFile == None:
        print(parser.usage)
        exit(0)
    pcapFile = options.pcapFile
    f = open(pcapFile)
    pcap = dpkt.pcap.Reader(f)
    printPcap(pcap)

if __name__ == "__main__":
    main()