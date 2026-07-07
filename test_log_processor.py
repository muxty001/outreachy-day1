import os
from log_processor import append_and_read_log

def test_log_lifecycle():
    test_file = "temp_test_log.txt"
    
    content = append_and_read_log(test_file, "Day 9: Mastering context managers.")
    
    assert "Day 9: Mastering context managers." in content
    
    if os.path.exists(test_file):
        os.remove(test_file)