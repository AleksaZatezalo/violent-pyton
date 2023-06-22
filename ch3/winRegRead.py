"""
Author: Aleksa Zatezalo
Description: File created to read the windows registry and print networks connected too.
Date: June 20, 2023
"""

from _winreg import *

def val2addr(val):
    """
    Converts a REG_BINARY string, val, into a MAC address. Retruns the MAC address.
    """
    
    addr = ""
    for ch in val:
        addr += ("%02x " % ord(ch))
    addr = addr.strip(" ").replace(" ", ":")[0:17]
    return addr


def printNets():
    """
    Prints the network information of all the networks the PC has connected to.
    """
    net = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    key = OpenKey(HKEY_LOCAL_MACHINE, net)
    print("\n[*] Networks You have Joined.")
    for i in range(100):
        try:
            guid = EnumKey(key, i)
            netKey = OpenKey(key, str(guid))
            (n, addr, t) = EnumValue(netKey, 5)
            (n, name, t) = EnumValue(netKey, 4)
            macAddr = val2addr(addr)
            netName = str(name)
            print("[+] " + netName + " " + macAddr)
        except:
            break


def main():
    printNets()

if __name__ == "__main__":
    main()