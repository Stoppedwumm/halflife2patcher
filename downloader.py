from utils import *

def Download(skipHomebrew: bool = False, skipSourceEngine: bool = False, skipDeps: bool = False, repoURL: str = "https://github.com/nillerusr/source-engine"):
    print("Preparing files...")

    sFolderExists = os.path.isdir('source-engine')
    hbFolderExists = os.path.isdir("/opt/homebrew")

    print("Installing XCode and Homebrew, please accept any licenses, warnings etc...")
    exec("xcode-select --install")
    if not hbFolderExists and not skipHomebrew:
        exec('NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        print("Installed Homebrew! Please restart your terminal...")
        exit(0)

    if not skipDeps:
        exec("brew install git")
        exec("brew install sdl2 freetype2 fontconfig pkg-config opus libpng libedit")

    if not sFolderExists and not skipSourceEngine:
        exec(f"git clone {repoURL} --recursive")