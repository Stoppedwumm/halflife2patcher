import os
def exec(command: str):
    """
    Execute a shell command

    Args:
        command (str): The command to execute
    """
    return os.system(command)