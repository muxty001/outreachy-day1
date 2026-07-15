import csv
import json
from typing import List

def filter_passing_students(csv_path: str, config_path: str) -> List[str]:
    """
    Reads scores from a CSV file and a passing threshold from a JSON config file.
    Returns a list of student names who met or exceeded the threshold.
    """
    try:
        with open(config_path, "r", encoding="utf-8") as json_file:
            config = json.load(json_file)
        threshold = config.get("passing_threshold", 50.0)
        
        passing_students = []
        with open(csv_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            
            for row in reader:
                if float(row["score"]) >= threshold:
                    passing_students.append(row["name"])
                    
        return passing_students
        
    except (FileNotFoundError, KeyError, ValueError, json.JSONDecodeError):
        return []