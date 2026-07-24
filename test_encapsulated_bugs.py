import pytest
from encapsulated_bugs import StrictBug, InvalidSeverityError

def test_valid_severity_assignment():
    bug = StrictBug("BUG-501", "Memory leak in service", "High")
    assert bug.get_severity() == "High"

    bug.set_severity("Critical")
    assert bug.get_severity() == "Critical"

def test_invalid_severity_raises_exception():
    bug = StrictBug("BUG-502", "Minor typo in UI", "Low")
    with pytest.raises(InvalidSeverityError):
        bug.set_severity("Extreme")  
    assert bug.get_severity() == "Low"