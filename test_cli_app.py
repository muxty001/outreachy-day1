from issue_repository import IssueRepository
from cli_app import run_issue_cli

def test_cli_add_and_get():
    repo = IssueRepository()
    
    add_payload = {"bug_id": "BUG-701", "title": "OAuth crash", "severity": "Critical"}
    add_result = run_issue_cli(repo, "ADD", add_payload)
    assert "Success" in add_result
    
    get_payload = {"bug_id": "BUG-701"}
    get_result = run_issue_cli(repo, "GET", get_payload)
    assert "[BUG-701] OAuth crash (Critical)" in get_result

def test_cli_invalid_command():
    repo = IssueRepository()
    result = run_issue_cli(repo, "DELETE", {})
    assert "Error: Unknown command 'DELETE'." in result

def test_cli_filter():
    repo = IssueRepository()
    run_issue_cli(repo, "ADD", {"bug_id": "BUG-702", "title": "Typo", "severity": "Low"})
    
    filter_result = run_issue_cli(repo, "FILTER", {"severity": "Low"})
    assert "Found 1 bug(s) with severity 'Low'." in filter_result