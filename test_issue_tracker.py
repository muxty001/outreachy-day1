from issue_tracker import Issue, Bug, FeatureRequest

def test_generic_issue_summary():
    issue = Issue("SYS-101", "Server reboot required")
    assert issue.get_summary() == "[SYS-101] Server reboot required"

def test_bug_summary_override():
    bug = Bug("BUG-302", "Session timeout", "High")
    assert bug.get_summary() == "[BUG-302] Session timeout | Severity: High"

def test_feature_summary_override():
    feature = FeatureRequest("FEAT-404", "Add Dark Mode", "Medium")
    assert feature.get_summary() == "[FEAT-404] FEATURE: Add Dark Mode (Priority: Medium)"