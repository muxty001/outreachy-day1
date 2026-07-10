import os
import json
from config_manager import update_json_config

def test_json_update_lifecycle():
    test_file = "settings.json"
    initial_data = {"theme": "light", "version": 1.0}
    
    # Create a temporary JSON file to test with
    with open(test_file, "w", encoding="utf-8") as file:
        json.dump(initial_data, file)
        
    # Run our function to update the theme to dark
    updated_result = update_json_config(test_file, "theme", "dark")
    
    # Assertions
    assert isinstance(updated_result, dict)
    assert updated_result["theme"] == "dark"
    assert updated_result["version"] == 1.0
    
    # Clean up the disk file
    if os.path.exists(test_file):
        os.remove(test_file)