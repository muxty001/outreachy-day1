from typing import Dict, Any

class Issue:
    def __init__(self, issue_id: str, title: str):
        self.issue_id = issue_id
        self.title = title
        self.status = "open"

    def resolve(self) -> None:
        self.status = "Resolved"

class Bug(Issue):
    def __init__(self, issue_id: str, title: str, severity):
        super().__init__(issue_id, title)
        self.severity = severity

class FeatureRequest(Issue):
    def __init__(self, issue_id: str, title: str, target_version: str):
        super().__init__(issue_id, title)
        self.target_version = target_version
        self.priority = "Medium"