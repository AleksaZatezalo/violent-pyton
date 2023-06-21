"""
Author: Aleksa Zatezalo
Description: File created to read the windows registry.
Date: June 20, 2023
"""

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
    pass


def main():
    pass

if __name__ == "__main__":
    p