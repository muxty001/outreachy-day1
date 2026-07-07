from typing import Union

def append_and_read_log(file_path: str, message: str) -> Union[str, bool]:
    """
    Appends a new log message to a file, then reads the entire file content back. 
    """
    try:
        with open(file_path, "a+", encoding="utf-8") as file:
            file.write(message + "\n")
            file.seek(0)
            return file.read()
        
    except IOError:
        return "Error: Could not read or write to the specified file."