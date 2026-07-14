import os
from data_parser import calculate_average_from_csv

def test_csv_average_calculation():
    test_file = "test_scores.csv"
    
    with open(test_file, "w", encoding="utf-8") as file:
        file.write("name,score\n")
        file.write("Alice,85.0\n")
        file.write("Bob,95.0\n")
        
 
    average = calculate_average_from_csv(test_file)
    
    assert average == 90.0
    
    if os.path.exists(test_file):
        os.remove(test_file)

def test_csv_missing_file():
    assert calculate_average_from_csv("not_a_real_file.csv") == 0.0