from utils import *

def Build():
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