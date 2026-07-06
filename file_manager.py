import os
from typing import List, Union

def list_directory_contents(dir_path: str) -> Union[List[str], str]:
    """
    Safely scans a directory path and returns a list of its filenames.
    If the path does not exist, returns a safe error string.
    """
    try:
        return os.listdir(dir_path)
         
    except FileNotFoundError:
        return "Error: The specified directory does not exist."