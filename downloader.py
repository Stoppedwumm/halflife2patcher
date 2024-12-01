from utils import *

def Download(skipHomebrew: bool = False, skipSourceEngine: bool = False, skipDeps: bool = False, repoURL: str = "https://github.com/nillerusr/source-engine"):
    """
    Prepares the environment for building the source engine by installing necessary dependencies.

    Args:
        skipHomebrew (bool): If True, skips installing Homebrew. Defaults to False.
        skipSourceEngine (bool): If True, skips cloning the source engine repository. Defaults to False.
        skipDeps (bool): If True, skips installing dependencies via Homebrew. Defaults to False.
        repoURL (str): The URL of the source engine repository to clone. Defaults to "https://github.com/nillerusr/source-engine".

    This function will attempt to install XCode command line tools, Homebrew, and various dependencies
    needed for building the source engine unless specified otherwise by the arguments. It will also 
    clone the source engine repository if it does not already exist.
    """
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