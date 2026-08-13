from encapsulated_bugs import StrictBug, InvalidSeverityError
from issue_repository import IssueRepository

def run_issue_cli(repo: IssueRepository, user_command: str, payload: dict) -> str:
    """
    Acts as a controller handling user commands for the issue tracker.
    
    Commands supported:
    - 'ADD': Creates and stores a new StrictBug.
    - 'GET': Retrieves a bug by ID.
    - 'FILTER': Returns a count of bugs matching a severity level.
    """
    if user_command == "ADD":
        try:
            bug = StrictBug(
                bug_id=payload["bug_id"],
                title=payload["title"],
                severity=payload["severity"]
            )
            repo.add_bug(bug)
            return f"Success: Bug {bug.bug_id} added."
        except (InvalidSeverityError, KeyError) as error:
            return f"Error: Failed to add bug. Details: {error}"

    elif user_command == "GET":
        bug_id = payload.get("bug_id")
        bug = repo.get_bug(bug_id)
        if not bug:
            return f"Error: Bug {bug_id} not found."
        return f"[{bug.bug_id}] {bug.title} ({bug.get_severity()})"

    elif user_command == "FILTER":
        severity = payload.get("severity")
        matching = repo.get_bugs_by_severity(severity)
        return f"Found {len(matching)} bug(s) with severity '{severity}'."

    else:
        return f"Error: Unknown command '{user_command}'."