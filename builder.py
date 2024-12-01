from utils import *
def Build(game: str = "hl2", dest: str = "hl2"):
    """
    Builds and installs the given game from the source engine, defaulting to half-life 2.
    
    Args:
        game (str): The game to build. Defaults to "hl2".
        dest (str): The destination directory for the built game. Defaults to "hl2".
    """
    print("Configuring build...")
    # Run in source engine dir
    exec(f"cd source-engine && python3 waf configure -T release --prefix='' --build-games={game}")

    print("Building...")

    # Run in source engine dir
    exec("cd source-engine && python3 waf build")

    print("Installing...")

    # Run in source engine dir
    exec(f"cd source-engine && python3 waf install --destdir='{dest}'")

    print("Patch built!")