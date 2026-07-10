import json
from typing import Dict, Any, Union

def update_json_config(file_path: str, key: str, value: Any) -> Union[Dict[str, Any], str]:
    """
    Safely reads a JSON file, updates a specific configuration key, 
    saves it back to the file, and returns the updated dictionary.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            config_data = json.load(file)
        
        config_data[key] = value
        
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(config_data, file, indent=4)
            
        return config_data
        
    except (FileNotFoundError, json.JSONDecodeError):
        return "Error: Could not process configuration file."