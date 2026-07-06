import os
from file_manager import list_directory_contents

def test_scan_current_directory():
    result = list_directory_contents(".")
    assert isinstance(result, list)
    assert "file_manager.py" in result

def test_scan_non_existent_directory():
    fake_path = "C:/Users/HP/Documents/this-folder-does-not-exist-12345"
    assert list_directory_contents(fake_path) == "Error: The specified directory does not exist."