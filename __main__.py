import os

def exec(command: str):
    os.system(command)

print("Half Life 2 Patcher")
print("Version 0.0.1")
print("Written by Stoppedwumm")
print("Source Engine: https://github.com/nillerusr/source-engine")

input("Before starting, make sure you have Python 3.11 installed and that you have git installed. As of 2024, you need to enable in the properties of Half Life 2 the beta 'steam_legacy - Pre-20th Anniversary Build'. Press enter to continue...")

print("Preparing files...")

folderExists = os.path.isdir('source-engine')

if not folderExists:
    exec("git clone https://github.com/nillerusr/source-engine --recursive")

print("Configuring build...")

# Run in source engine dir
exec("cd source-engine && python3 waf configure -T release --prefix='' --build-games=hl2")

print("Building...")

# Run in source engine dir
exec("cd source-engine && python3 waf build")

print("Installing...")

# Run in source engine dir
exec("cd source-engine && python3 waf install --destdir='hl2'")

print("Patch built!")

res = ""

while True:
    halfLife2Path = input("Enter the path to Half-Life 2 or press ? for help: ")

    if halfLife2Path != "?":
        res = halfLife2Path
        break

    print("Enter the full path to your Half-Life 2 path, you can navigate to the folder by clicking 'Half-Life 2 => Right Click => Manage => Browse Local Files'. After you've copied the path (search online), paste it here.")

print("Patching...")

# Replace files over: source-engine/hl2 => bin, hl2/bin
# Copy over hl2_launcher and rename it hl2_osx
patchedPath = "source-engine/hl2"
binList = ['bin', 'hl2/bin']

if res.endswith("/"):
    res = res[:-1]

# Replace the files in the halfLifePath
for bin in binList:
    print(f"cp -r '{patchedPath}/{bin}' '{res}/{bin}'")
    exec(f"cp -r '{patchedPath}/{bin}' '{res}/{bin}'")

# Copy over hl2_launcher and rename it hl2_osx
print(f"cp '{patchedPath}/hl2_launcher' '{res}/hl2_osx'")
exec(f"cp '{patchedPath}/hl2_launcher' '{res}/hl2_osx'")

print("Patched!")