"""
Author: Aleksa Zatezalo
Description: Script created to recover deleted items.
Date: June 20, 2023
"""

import os
from _winreg import *

def returnDir():
    """
    Returns the directory of the Recycling bin.
    """
    
    dirs = ['C:\\Recycler', "C:\\Recycled\\", "C:\\$Recycle.Bin\\"]
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None

def sid2user(sid):
    """
    Correleates SID to user.
    """
    try: 
        key = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\\" + sid)
        (value, type) = QueryValueEx(key, 'ProfileImagePath')
        user = value.split('\\')[-1]
        return user
    except:
        return sid

def findRecycled(recycleDir):
    """
    Find recycled files.
    """
    dirList = os.listdir(recycleDir)
    for sid in dirList:
        files = os.listdir(recycleDir + sid)
        user = sid2user(sid)
        print('[*] Listing Files For User: ' + str(user))
        for file in files:
            print("[+] Found File: " + str(file))

def main():
    recycled = returnDir()
    findRecycled(recycled)

if __name__ == '__main__':
    main()