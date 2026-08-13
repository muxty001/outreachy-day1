from encapsulated_bugs import StrictBug
from issue_repository import IssueRepository

def test_repository_add_and_get():
    repo = IssueRepository()
    bug = StrictBug("BUG-601", "API Latency spike", "High")
    
    repo.add_bug(bug)
    retrieved = repo.get_bug("BUG-601")
    
    assert retrieved is not None
    assert retrieved.title == "API Latency spike"

def test_repository_severity_filtering():
    repo = IssueRepository()
    repo.add_bug(StrictBug("BUG-602", "UI alignment", "Low"))
    repo.add_bug(StrictBug("BUG-603", "Database deadlock", "Critical"))
    repo.add_bug(StrictBug("BUG-604", "Auth bypass", "Critical"))

    critical_bugs = repo.get_bugs_by_severity("Critical")
    
    assert len(critical_bugs) == 2
    assert critical_bugs[0].bug_id in ["BUG-603", "BUG-604"]

def test_repository_serialization():
    repo = IssueRepository()
    repo.add_bug(StrictBug("BUG-605", "Memory leak", "Medium"))

    serialized = repo.to_dict_list()
    
    assert len(serialized) == 1
    assert serialized[0] == {
        "bug_id": "BUG-605",
        "title": "Memory leak",
        "severity": "Medium"
    }