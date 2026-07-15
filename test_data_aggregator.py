import os
import json
from data_aggregator import filter_passing_students

def test_pipeline_integration():
    csv_file = "temp_student_scores.csv"
    json_file = "temp_threshold_config.json"

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump({"passing_threshold": 80.0}, f)
    with open(csv_file, "w", encoding="utf-8") as f:
        f.write("name,score\n")
        f.write("Alice,75.0\n")    # Fails (75 < 80)
        f.write("Bob,85.0\n")      # Passes (85 >= 80)
        f.write("Charlie,92.5\n")  # Passes (92.5 >= 80)
        
    try:
        passing_list = filter_passing_students(csv_file, json_file)
        assert passing_list == ["Bob", "Charlie"]
        
    finally:
        if os.path.exists(csv_file):
            os.remove(csv_file)
        if os.path.exists(json_file):
            os.remove(json_file)