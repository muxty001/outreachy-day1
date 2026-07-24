from typing import List

class InvalidSeverityError(Exception):
    """Raised when a severity level is assigned that isn't supported."""
    pass

class StrictBug:
    ALLOWED_SEVERITIES: List[str] = ["Low", "Medium", "High", "Critical"]

    def __init__(self, bug_id: str, title: str, severity: str):
        self.bug_id = bug_id
        self.title = title
        self._severity = ""
        self.set_severity(severity)

    def get_severity(self) -> str:
        """Getter method to safely read the private severity."""
        return self._severity

    def set_severity(self, new_severity: str) -> None:
        """Setter method that guards against invalid inputs."""
        if new_severity not in self.ALLOWED_SEVERITIES:
            raise InvalidSeverityError(
                f"'{new_severity}' is not valid. Allowed: {self.ALLOWED_SEVERITIES}"
            )
        self._severity = new_severity