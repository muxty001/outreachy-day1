import csv
from typing import List

def calculate_average_from_csv(file_path: str) -> float:

    """
    Reads a CSV file containing columns 'name' and 'score', and returns the average score as a float
    """

    try:
        total_score = 0.0
        count = 0

        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader: 
                total_score += float(row["score"])
                count += 1
        if count == 0:
            return 0.0

        return total_score / count
    
    except (FileNotFoundError, KeyError, ValueError):
        return 0.0