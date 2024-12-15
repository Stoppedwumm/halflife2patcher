import sys
from builder import *
from utils import *
from downloader import *
from patcher import *
import threading

print("Half Life 2 Patcher")
print("Version 1.1.0")
print("Written by Stoppedwumm")
print("Source Engine: https://github.com/nillerusr/source-engine")
pregrabbedPath = ""

if sys.argv.count("--debug") != 1:
    input("Before starting, make sure you have Python 3.11 installed and that you have git installed. As of 2024, you need to enable in the properties of Half Life 2 the beta 'steam_legacy - Pre-20th Anniversary Build'. Press enter to continue...")
else:
    print("Skipping input...")

#if sys.argv.count("--debug") == 1:
Download()

Build()
"""
else:
    data = {
        "download": False,
        "path": "",
    }
    lock = threading.Lock()
    threading.Thread(target=gui.GUIThread, args=(data, lock)).start()
    while True:
        if data["download"] == True:
            pregrabbedPath = data["path"]
            break
    Download()
    Build()
"""
        
    

if pregrabbedPath != "":
    Patcher(pregrabbedPath)
else:
    res = ""
    if sys.argv.count("--debug") == 1:
        print("Build in debug mode done! Exiting early...")
        exit(0)

    defaultInstall = False
    otherInstall = False
    customInstall = False

    choice = input("Do you want to install the patched files in the default location on your main drive? You can also change the drive to look on with other. (y/n/other) ")

    if choice == "y" or choice == "Y":
        defaultInstall = True
    elif choice == "n" or choice == "N":
        customInstall = True
    else:
        otherInstall = True

    if customInstall:
        while True:
            halfLife2Path = input("Enter the path to Half-Life 2 or press ? for help: ")

            if halfLife2Path != "?":
                res = halfLife2Path
                break

            print("Enter the full path to your Half-Life 2 path, you can navigate to the folder by clicking 'Half-Life 2 => Right Click => Manage => Browse Local Files'. After you've copied the path (search online), paste it here.")
    elif otherInstall:
        while True:
            halfLife2Path = input("Enter the Drive Name where Half Life 2 is installed: ")

            if halfLife2Path != "?":
                res = "/Volumes/" + halfLife2Path + "/SteamLibrary/steamapps/common/Half-Life 2"
                break
    elif defaultInstall:
        if os.path.isdir(os.path.expanduser("~/Library/Application Support/Steam/steamapps/common/Half-Life 2")):
            res = "~/Library/Application Support/Steam/steamapps/common/Half-Life 2"
        elif os.path.isdir(os.path.expanduser("~/.steam/steam/steamapps/common/Half-Life 2")):
            res = "~/.steam/steam/steamapps/common/Half-Life 2"
        else:
            raise ValueError("Could not find Half-Life 2 path.")
    else:
        raise ValueError("Incorrect input.")
        

    Patcher(res)

