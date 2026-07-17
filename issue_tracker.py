class Issue:
    def __init__(self, issue_id: str, title: str):
        self.issue_id = issue_id
        self.title = title

    def get_summary(self) -> str:
        """Default parent summary format."""
        return f"[{self.issue_id}] {self.title}"


class Bug(Issue):
    def __init__(self, issue_id: str, title: str, severity: str):
        super().__init__(issue_id, title)
        self.severity = severity

    def get_summary(self) -> str:
        """
        Overrides the parent method to include the severity badge.
        """
        parent_summary = super().get_summary()
        return f"{parent_summary} | Severity: {self.severity}"


class FeatureRequest(Issue):
    def __init__(self, issue_id: str, title: str, priority: str):
        super().__init__(issue_id, title)
        self.priority = priority

    def get_summary(self) -> str:
        """
        Overrides the parent method to show the feature priority.
        """
        return f"[{self.issue_id}] FEATURE: {self.title} (Priority: {self.priority})"