from bug_tracker import Bug

def test_bug_initialization():
    bug = Bug("BUG-101", "Database timeout under high load", "High")
    assert bug.bug_id == "BUG-101"
    assert bug.status == "Open"

def test_bug_resolution():
    bug = Bug("BUG-102", "CSS alignment issue on landing page", "Low")
    bug.resolve()
    
    assert bug.status == "Resolved"

def test_bug_to_dict_conversion():
    bug = Bug("BUG-103", "Auth token memory leak", "Critical")
    exported_data = bug.to_dict()
    assert exported_data["status"] == "Open"
    assert exported_data["severity"] == "Critical"