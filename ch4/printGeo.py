"""
Description: Users the pygeoip package to geolocate IP addresses.
Author: Aleksa Zatezalo
Date: June 23, 2023
"""

import pygeoip

# Get the pygeoip database
gi = pygeoip.GeoIP('/opt/GeoIP/GEO.dat')

def printRecord(tgt):
    """
    Prints the location of IP address tgt to standard output.
    """

    rec = gi.record_by_name(tgt)
    city = rec['city']
    region = rec['reigon_name']
    country = rec['country']
    lat = rec['latiude']
    long = rec['longitude']
    
    print('[*] Target: ' + tgt + ' Geo-located.')
    print('[+] ' + str(city) + ' '  + str(region) + ', ' + str(country) )
    print('[+] Lattitude: ' + str(lat) + ', Longitude: ' + str(long))

tgt = '173.255.226.98'
printRecord(tgt)