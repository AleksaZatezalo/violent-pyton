"""
Description: A Zip file cracker written in python.
Author: Aleksa Zatezalo
Date: June 18th, 2022
"""

import zipfile
import optparse
from threading import Thread

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print('[+] Found password ' + password + '\n')
    except:
        pass
    
def main():
    parser = optparse.OptionParser("usage%prog " + "-f <zipFile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionaru file')
    (options, args) = parser.parse_args()
    if (options.zname == None) or (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(dname)
    passFile = open(zname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

if __name__ == '__main__':
    main()