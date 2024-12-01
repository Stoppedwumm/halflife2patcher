from utils import *

def Patcher(result: str):
    """
    Patches the Half-Life 2 game by replacing specific directories and files with the patched versions.

    Args:
        result (str): The path to the Half-Life 2 installation directory where the patches will be applied.

    This function copies the 'bin' directories from the 'source-engine/hl2' to the specified Half-Life 2 directory.
    It also copies the 'hl2_launcher' file from the 'source-engine/hl2' directory and renames it to 'hl2_osx' in the
    specified Half-Life 2 directory.
    """
    print("Patching...")
    res = result
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