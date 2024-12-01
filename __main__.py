import sys
from builder import *
from utils import *
from downloader import *
from patcher import *

print("Half Life 2 Patcher")
print("Version 0.0.1")
print("Written by Stoppedwumm")
print("Source Engine: https://github.com/nillerusr/source-engine")

if sys.argv[1] != "--debug":
    input("Before starting, make sure you have Python 3.11 installed and that you have git installed. As of 2024, you need to enable in the properties of Half Life 2 the beta 'steam_legacy - Pre-20th Anniversary Build'. Press enter to continue...")
else:
    print("Skipping input...")

Download()

Build()

res = ""

if sys.argv[1] == "--debug":
    print("Build in debug mode done! Exiting early...")
    exit(0)

defaultInstall = False
otherInstall = False

if os.path.isdir("~/Library/Application Support/Steam/SteamApps"):
    choice = input("Do you want to install the patched files in the default location on your main drive? You can also change the drive to look on with other. (y/n/other) ")

    if choice == "y" or choice == "Y":
        defaultInstall = True
    elif choice == "n" or choice == "N":
        pass
    else:
        otherInstall = True

if not defaultInstall:
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
else:
    res = "~/Library/Application Support/Steam/SteamApps/common/Half-Life 2"

Patcher(res)