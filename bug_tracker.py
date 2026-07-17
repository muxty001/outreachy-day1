from typing import Dict, Any

class Bug:
    """
    Represents a software bug report in an issue tracker.
    """
    def __init__(self, bug_id: str, description: str, severity: str):
        self.bug_id = bug_id
        self.description = description
        self.severity = severity
        self.status = "Open"  # Default initial state

    def resolve(self) -> None:
        """Marks the bug as resolved."""
        self.status = "Resolved"

    def update_severity(self, new_severity: str) -> None:
        """Safely updates the bug severity."""
        self.severity = new_severity

    def to_dict(self) -> Dict[str, Any]:
        """Converts the class instance state into a clean dictionary."""
        return {
            "id": self.bug_id,
            "description": self.description,
            "severity": self.severity,
            "status": self.status
        }