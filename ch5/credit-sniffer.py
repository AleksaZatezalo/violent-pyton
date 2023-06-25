"""
Description: A python program used to sniff credit card numbers in wireless packets.
Author: Aleksa Zatezalo
Date: June 23, 2023
"""

import re

def findCreditCard(raw):
    americaRE = re.findall('3[47][0-9]{13}', raw)
    if americaRE:
        print("[+] Found American Express Card: " + americaRE[0])

def main():
    tests = []
    tests.append("I would like 1337 coppies of that dvd")
    tests.append("Bill my card: 378282246310005 for \$2600")
    for test in tests:
        findCreditCard(test)