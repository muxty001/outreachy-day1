from typing import Dict, List, Optional
from encapsulated_bugs import StrictBug

class IssueRepository:
    """
    Manages a collection of StrictBug objects in memory.
    """
    def __init__(self):
        self._bugs: Dict[str, StrictBug] = {}

    def add_bug(self, bug: StrictBug) -> None:
        """Adds a bug to the repository."""
        self._bugs[bug.bug_id] = bug

    def get_bug(self, bug_id: str) -> Optional[StrictBug]:
        """Retrieves a bug by ID, returning None if missing."""
        return self._bugs.get(bug_id)

    def get_bugs_by_severity(self, severity: str) -> List[StrictBug]:
        """Filters stored bugs matching a target severity."""
        return [
            bug for bug in self._bugs.values()
            if bug.get_severity() == severity
        ]

    def to_dict_list(self) -> List[Dict[str, str]]:
        """Serializes all managed objects into a list of dictionaries."""
        return [
            {
                "bug_id": bug.bug_id,
                "title": bug.title,
                "severity": bug.get_severity()
            }
            for bug in self._bugs.values()
        ]