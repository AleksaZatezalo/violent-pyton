"""
Author: Aleksa Zatezalo
Description: A Unix password cracker in python.
Date: June 9, 2023
"""

import crypt

def testPass(cryptPass):
    """
    Takes a encrypted password, cryptPass, and runs a dictionary attack on it.
    Prints found password to standard output. Returns a boolean.
    """

    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word.salt)
        if (cryptWord == cryptPass):
            print("[+] Found Password: " +word+"\n")
            return True
    print("[-] Password Not Found. \n")
    return False

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print("[*] Cracking Password For: " + user)
            testPass(cryptPass)

if __name__ == "__main__":
    main()